from CNNClassifier.components import stage_01_data_ingestion
from CNNClassifier. config import ConfigurationManager
from CNNClassifier import logger

config=ConfigurationManager()
data_ingestion_config=config.get_data_ingestion_config()

data_ingestion=DataIngestion(config=data_ingestion_config)

STAGE_NAME = "Data Ingestion stage"

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.unzip_and_clean()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e