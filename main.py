from src.ETE_wine_quality import logger
from src.ETE_wine_quality.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.ETE_wine_quality.pipeline.data_validation_pipeline import DataValidatioTrainingPipeline
from src.ETE_wine_quality.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.ETE_wine_quality.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.ETE_wine_quality.pipeline.model_evaluation_pipeline import ModelEvalutionTrainingPipeline

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
    data_validation=DataValidatioTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>stage {STAGE_NAME} started <<<<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME="Data Trainer Stage"
try:
    logger.info(f">>>>>>>>>stage {STAGE_NAME} started <<<<<<<")
    model_training=ModelTrainerTrainingPipeline()
    model_training.initiate_model_training()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e  

STAGE_NAME="Data Evalution Stage"
try:
    logger.info(f">>>>>>>>>stage {STAGE_NAME} started <<<<<<<")
    model_evalution=ModelEvalutionTrainingPipeline()
    model_evalution.initiate_model_evalution()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e  