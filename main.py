from src.ETE_wine_quality import logger
from src.ETE_wine_quality.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.ETE_wine_quality.pipeline.data_validation_pipeline import DataValidatioTrainingPipeline



STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>stage {STAGE_NAME} started <<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e    

STAGE_NAME="Data Validaton Stage"
try:
    logger.info(f">>>>>>>>>stage {STAGE_NAME} started <<<<<<<")
    data_ingestion=DataValidatioTrainingPipeline()
    data_ingestion.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e  