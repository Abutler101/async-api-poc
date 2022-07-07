import json
import uuid

from redis import Redis
from pydantic import BaseSettings
from loguru import logger

from src.task_management.helpers import get_task_id
from src.task_management.models import TaskId, DelayedResource, TaskType, TaskContext


class RedisConfig(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 6379
    password: str

    class Config:
        env_prefix = "redis_"


def create_client(connection_config: RedisConfig = RedisConfig()) -> Redis:
    return Redis(
        host=connection_config.host,
        port=connection_config.port,
        password=connection_config.password,
    )


def register_task(task_type: TaskType, context: TaskContext) -> TaskId:
    task_id: TaskId = get_task_id(context, task_type)
    task: DelayedResource = DelayedResource(
        type=task_type, optimizationId=context.optimizationId, modelId=context.modelId
    )
    client = create_client()
    client.set(task_id, task.json())
    return task_id


def get_task(task_id: TaskId) -> DelayedResource:
    client = create_client()
    raw_result = json.loads(client.get(task_id))
    return DelayedResource.parse_raw(raw_result)


def cache_task_output(task_id: TaskId, body: DelayedResource):
    client = create_client()
    client.delete(task_id)
    client.set(task_id, body.json())
