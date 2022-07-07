from enum import Enum
from typing import TypeVar

from pydantic import BaseModel, Extra

# ─────────────────────────────── Generic Models ────────────────────────────── #
TaskId = TypeVar(name="TaskId", bound=str)


class TaskType(str, Enum):
    FEATURE_IMPORTANCE = "feature_importance"
    PIPELINE_ZIP = "pipeline_zip"


class DelayedResource(BaseModel):
    optimizationId: str
    modelId: str
    type: TaskType

    class Config:
        extra = Extra.allow


class TaskContext(BaseModel):
    optimizationId: str
    modelId: str


# ────────────────────────── Specific Task Resources ────────────────────────── #
class FeatureImportance(DelayedResource):
    type: TaskType = TaskType.FEATURE_IMPORTANCE
    prettyGraph: dict = {"Graphs": "aren't", "that": "pretty"}


class ProjectZip(DelayedResource):
    type: TaskType = TaskType.PIPELINE_ZIP
    fileId: str
