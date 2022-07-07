import uuid

from src.task_management.models import TaskContext, TaskType, TaskId


def get_task_id(context: TaskContext, type: TaskType) -> TaskId:
    # TODO: make deterministic and deal with multiple simultaneous
    return uuid.uuid4().hex
