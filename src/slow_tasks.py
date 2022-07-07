import time
import random
import uuid

from loguru import logger
from pydantic import BaseModel


class DelayedResource(BaseModel):
    optimizationId: str
    modelId: str
    type: str


class FeatureImportance(DelayedResource):
    type: str = "FeatureImportance"
    prettyGraph: dict = {"Graphs": "aren't", "that": "pretty"}


class ProjectZip(DelayedResource):
    type: str = "PipelineZip"
    fileId: str


def send_notification(task_id: str, resource: DelayedResource):
    logger.info(
        f"Sent notification to Kafka for resource of type: {resource.type} "
        f"on optimization {resource.optimizationId} for model: {resource.modelId}"
        f"resulting from task_id: {task_id}"
    )
    pass


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
