import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlproject.entity.config_entity import DataTransformationConfig


import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder,LabelEncoder,StandardScaler




class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def processor(self):
        le =LabelEncoder()
        oe = OrdinalEncoder()
        ohe = OneHotEncoder()
        ss = StandardScaler()

        data = pd.read_csv(self.config.data_path,sep=";")

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data,test_size=0.2,random_state=42)
        train['y_enc']=le.fit_transform(train['y'])
        test['y_enc']=le.fit_transform(test['y'])

        std_cols = ['age','duration','emp.var.rate', 'cons.price.idx',
       'cons.conf.idx', 'euribor3m', 'nr.employed']
        
        cat_cols = ['job', 'marital', 'education', 'default',
       'contact', 'month', 'day_of_week','poutcome']
        
        other_cols = ['campaign','pdays','previous']
        target = ['y']

        no_association_cols = ['housing','loan']

        #Preparation of train data
        ss = StandardScaler().fit(train[std_cols])
        train_std=pd.DataFrame(ss.transform(train[std_cols]),columns=std_cols,index=train.index)

        train['campaign_rec'] = 1/train['campaign']
        train['previous_plus1'] = train['previous']+1

        train_cat = pd.get_dummies(train[cat_cols])
        train = train.join(train_cat)

        drop_cols = ['job_unknown',
                'marital_unknown',
                'education_illiterate',
                'default_yes',
                'contact_telephone',
                'month_dec',
                'day_of_week_fri',
                'poutcome_failure'] + std_cols + cat_cols +['housing','loan','pdays','campaign','previous']
        
        train.drop(columns=drop_cols,axis=1,inplace=True)

        train = train.join(train_std)

        selected_cols =['campaign_rec', 'job_admin.', 'job_entrepreneur', 'job_housemaid',
       'job_management', 'job_retired', 'job_services', 'job_student',
       'job_technician', 'job_unemployed', 'education_basic.4y',
       'education_basic.9y', 'education_high.school',
       'education_professional.course', 'education_unknown', 'default_unknown',
       'contact_cellular', 'month_apr', 'month_aug', 'month_jun', 'month_mar',
       'month_may', 'month_nov', 'day_of_week_mon', 'day_of_week_tue',
       'day_of_week_wed', 'poutcome_nonexistent', 'poutcome_success',
       'duration', 'emp.var.rate', 'cons.price.idx', 'euribor3m',
       'nr.employed','y_enc']
        
        train = train[selected_cols]
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        
        #Preparation of test data

        test_std=pd.DataFrame(ss.transform(test[std_cols]),columns=std_cols,index=test.index)

        test['campaign_rec'] = 1/test['campaign']
        test['previous_plus1'] = test['previous']+1

        test_cat = pd.get_dummies(test[cat_cols])
        test = test.join(test_cat)

        drop_cols_test = [i for i in drop_cols if i != 'default_yes']
        
        test.drop(columns=drop_cols_test,axis=1,inplace=True)

        test = test.join(test_std)

        #selected_cols_test =selected_cols+['default_yes']
        
        test = test[selected_cols]
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)