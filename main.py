from mlproject.pipeline.stage01_data_ingestion import DataIngestionPipeline
from mlproject import logger

STAGE_NAME = "Data Ingestion"


try:
             
    logger.info(">>>>> STARTED {STAGE_NAME} <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(">>>>> Completed {STAGE_NAME}  successfully   <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e