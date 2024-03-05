# from src.cnnClassifier import logger # it is also ok
# from cnnClassifier import logger

# logger.info("welcome to our custom log")

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

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
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<< \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e
