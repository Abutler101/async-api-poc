import uuid

from fastapi import FastAPI
from fastapi import BackgroundTasks

from slow_tasks import feature_importance, pipeline_zip
from src.task_management.models import TaskType, TaskContext
from src.task_management.redis import register_task

app = FastAPI()


@app.get("/{optimizationId}/{modelId}/FeatureImportance")
async def get_feature_importance(
    background_tasks: BackgroundTasks, optimizationId: str, modelId: str
):
    task_id = register_task(
        task_type=TaskType.FEATURE_IMPORTANCE,
        context=TaskContext(optimizationId=optimizationId, modelId=modelId),
    )
    background_tasks.add_task(
        feature_importance,
        **{"task_id": task_id, "optimization_id": optimizationId, "model_id": modelId}
    )
    return {"taskId": task_id}


@app.get("/{optimizationId}/{modelId}/PipelineZip")
async def get_pipeline_zip(
    background_tasks: BackgroundTasks, optimizationId: str, modelId: str
):
    task_id = register_task(
        task_type=TaskType.PIPELINE_ZIP,
        context=TaskContext(optimizationId=optimizationId, modelId=modelId),
    )
    background_tasks.add_task(
        pipeline_zip,
        **{"task_id": task_id, "optimization_id": optimizationId, "model_id": modelId}
    )
    return {"taskId": task_id}
