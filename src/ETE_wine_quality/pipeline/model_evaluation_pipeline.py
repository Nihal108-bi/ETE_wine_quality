from src.ETE_wine_quality.config.configuration import ConfigurationManager
from src.ETE_wine_quality.components.model_evaluation import ModelEvaluation
from src.ETE_wine_quality import logger

STAGE_NAME = "Data evalution stage"
class ModelEvalutionTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_evalution(self):
        config = ConfigurationManager()
        model_evalution_config = config.get_model_evaluation_config()
        model_evalution = ModelEvaluation(config=model_evalution_config)
        model_evalution.log_into_mlflow()