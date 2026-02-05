from src.ETE_wine_quality.config.configuration import ConfigurationManager
from src.ETE_wine_quality.components.model_trainer import ModelTrainer
from src.ETE_wine_quality import logger

STAGE_NAME = "Data Trainer stage"
class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

  
