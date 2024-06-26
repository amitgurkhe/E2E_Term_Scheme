from mlproject.pipeline.stage01_data_ingestion import DataIngestionPipeline
from mlproject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from mlproject.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline
from mlproject import logger

STAGE_NAME = "Data Ingestion"


try:
             
    logger.info(f">>>>> STARTED {STAGE_NAME} <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>> Completed {STAGE_NAME}  successfully   <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e