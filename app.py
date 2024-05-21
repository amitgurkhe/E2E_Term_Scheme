import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
import joblib
from pathlib import Path

from mlproject.config.configuration import ConfigurationManager

from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel, Field


config = ConfigurationManager()
data_transformation_config = config.get_data_transformation_config()
data = pd.read_csv(data_transformation_config.data_path,sep=';')
train, test = train_test_split(data,test_size=0.2,random_state=42)
train = train.drop(columns='y',axis=1)

std_cols = ['age','duration','emp.var.rate', 'cons.price.idx',
       'cons.conf.idx', 'euribor3m', 'nr.employed']

cat_cols = ['job', 'marital', 'education', 'default',
       'contact', 'month', 'day_of_week','poutcome']

final_cols =['campaign_rec', 'job_admin.', 'job_entrepreneur', 'job_housemaid',
       'job_management', 'job_retired', 'job_services', 'job_student',
       'job_technician', 'job_unemployed', 'education_basic.4y',
       'education_basic.9y', 'education_high.school',
       'education_professional.course', 'education_unknown', 'default_unknown',
       'contact_cellular', 'month_apr', 'month_aug', 'month_jun', 'month_mar',
       'month_may', 'month_nov', 'day_of_week_mon', 'day_of_week_tue',
       'day_of_week_wed', 'poutcome_nonexistent', 'poutcome_success',
       'duration', 'emp.var.rate', 'cons.price.idx', 'euribor3m',
       'nr.employed']

def preprocessor(train,test,out_features,con_cols,cat_cols):
    
    test['campaign_rec'] = 1/test['campaign']
    test['previous_plus1'] = test['previous']+1
    
    ss=StandardScaler().fit(train[con_cols])
    oe = OneHotEncoder(handle_unknown='ignore').fit(train[cat_cols])
    
    test_std  = pd.DataFrame(ss.transform(test[con_cols]),columns=con_cols,index=test.index)
    oe_array_test = oe.transform(test[cat_cols]).toarray()
    oe_features = oe.get_feature_names_out(cat_cols)
    test_cat = pd.DataFrame(oe_array_test,columns=oe_features,index=test.index)
    
    test_drop = test.drop(columns=con_cols,axis=1)#,inplace=True)
    final_df = pd.concat([test_drop,test_std,test_cat],axis=1)
    return final_df[out_features]

model_path = 'artifacts\model_trainer\model.joblib'
with open(model_path, 'rb') as f:
    model = joblib.load(f)


app = FastAPI()

class PredictionInput(BaseModel):

    age : int
    job : object
    marital : object
    education : object
    default : object
    housing : object
    loan : object
    contact : object
    month : object
    day_of_week : object
    duration : int
    campaign : int
    pdays : int
    previous : int
    poutcome : object
    emp_var_rate: float = Field(..., alias="emp.var.rate")
    cons_price_idx: float = Field(..., alias="cons.price.idx")
    cons_conf_idx: float = Field(..., alias="cons.conf.idx")
    euribor3m: float
    nr_employed: float = Field(..., alias="nr.employed")
    #y : object


@app.get("/")
def home():
    return "Working fine"


@app.post("/predict")
def predict(input_data: PredictionInput):

    features=[input_data.age,
    input_data.job,
    input_data.marital,
    input_data.education,
    input_data.default,
    input_data.housing,
    input_data.loan,
    input_data.contact,
    input_data.month,
    input_data.day_of_week,
    input_data.duration,
    input_data.campaign,
    input_data.pdays,
    input_data.previous,
    input_data.poutcome,
    input_data.emp_var_rate,
    input_data.cons_price_idx,
    input_data.cons_conf_idx,
    input_data.euribor3m,
    input_data.nr_employed]
    
    print("list created")
    # data_dict = input_data.dict(by_alias=True)
    df = pd.DataFrame([features],columns=train.columns)

    print("dataframe created")

    processed_data = preprocessor(train,df,final_cols,std_cols,cat_cols)

    print(" preprocessor implemented")

    predictions = model.predict(processed_data)
    print("pred done")

    return {"prediction": predictions[0].item()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)