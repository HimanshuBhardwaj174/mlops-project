import mlflow
from mlflow.tracking import MlflowClient
import json
import dagshub
with open('reports/experiment_info.json','r') as f:
    content = json.load(f)
mlflow.set_tracking_uri('https://dagshub.com/HimanshuBhardwaj174/mlops-project.mlflow')

dagshub.init(repo_owner='HimanshuBhardwaj174', repo_name='mlops-project', mlflow=True)
run_id = content['run_id']
model_path = content['model_path']

uri = f"runs:/{run_id}/{model_path}"

model_name = 'dvc-pipeline'

result = mlflow.register_model(uri,model_name)

clinet = MlflowClient()

clinet.update_model_version(
    name=model_name,
    version=result.version,
    description='DVc pipeline best model'
)

clinet.set_model_version_tag(
    name=model_name,
    version=result.version,
    key='author',
    value='himanshu'
)

model_version= 1

new_stage = 'Production'

clinet.transition_model_version_stage(
    name=model_name,
    version=model_version,
    stage=new_stage,
    archive_existing_versions=True
)

