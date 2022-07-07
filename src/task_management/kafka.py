from loguru import logger

from src.task_management.models import DelayedResource, TaskId


def send_notification(task_id: TaskId, resource: DelayedResource):
    logger.info(
        f"Sent notification to Kafka saying resource of type: {resource.type} "
        f"on optimization {resource.optimizationId} for model: {resource.modelId}"
        f"resulting from task_id: {task_id} is available"
    )
    pass
