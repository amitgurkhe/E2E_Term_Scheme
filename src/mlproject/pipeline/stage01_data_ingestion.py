from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_ingestion import Dataingestion
from mlproject import logger


STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = Dataingestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            

if __name__ == '__main__':
      

      try:
             
        logger.info(">>>>> STARTED {STAGE_NAME} <<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(">>>>> Completed {STAGE_NAME}  successfully   <<<<<<<")
      except Exception as e:
           logger.exception(e)
           raise e

    
