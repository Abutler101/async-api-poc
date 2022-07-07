import time
import random
import uuid

from loguru import logger

from src.task_management.kafka import send_notification
from src.task_management.models import FeatureImportance, ProjectZip


def feature_importance(task_id: str, optimization_id: str, model_id: str) -> None:
    logger.debug("Entered Feature importance")
    time.sleep(random.randint(4, 20))
    result = FeatureImportance(optimizationId=optimization_id, modelId=model_id)
    send_notification(task_id, result)


def pipeline_zip(task_id: str, optimization_id: str, model_id: str) -> None:
    logger.debug("Entered Pipeline.zip generation")
    time.sleep(random.randint(4, 20))
    result = ProjectZip(
        optimizationId=optimization_id, modelId=model_id, fileId=str(uuid.uuid4())
    )
    send_notification(task_id, result)
