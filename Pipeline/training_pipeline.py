from zenml import pipelines
from Steps.ingest_data import ingest_df
from Steps.clean_data import clean_df
from Steps.model_train import train_model
from Steps.evaluation import evaluate_model


@Pipeline()
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)
    