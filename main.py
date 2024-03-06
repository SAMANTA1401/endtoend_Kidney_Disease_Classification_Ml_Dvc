# from src.cnnClassifier import logger # it is also ok
# from cnnClassifier import logger

# logger.info("welcome to our custom log")

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed successfully <<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e

    # 1:37:40


STAGE_NAME = "Prepare base model"

try:
    logger.info(f"************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    preapare_base_model = PrepareBaseModelTrainingPipeline()
    preapare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<< \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Training"
try:
    logger.info(f"*****************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
    model_trainer=ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\n x=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Evaluation stage"
try:
    logger.info(f"*********************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_evaluation=EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> {STAGE_NAME}  completed successfully! <<<<<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)
    raise e

