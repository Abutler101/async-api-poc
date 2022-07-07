import uuid

from fastapi import FastAPI
from fastapi import BackgroundTasks

from slow_tasks import feature_importance, pipeline_zip

app = FastAPI()


@app.get("/{optimizationId}/{modelId}/FeatureImportance")
async def get_feature_importance(
    background_tasks: BackgroundTasks, optimizationId: str, modelId: str
):
    task_id: str = uuid.uuid4().hex
    background_tasks.add_task(
        feature_importance,
        **{"task_id": task_id, "optimization_id": optimizationId, "model_id": modelId}
    )
    return {"taskId": task_id}


@app.get("/{optimizationId}/{modelId}/PipelineZip")
async def get_pipeline_zip(
    background_tasks: BackgroundTasks, optimizationId: str, modelId: str
):
    task_id: str = uuid.uuid4().hex
    background_tasks.add_task(
        pipeline_zip,
        **{"task_id": task_id, "optimization_id": optimizationId, "model_id": modelId}
    )
    return {"taskId": task_id}
