from mlproject.pipeline.stage01_data_ingestion import DataIngestionPipeline
from mlproject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
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