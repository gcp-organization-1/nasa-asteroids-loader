from google.cloud import bigquery
from config.settings import settings

class AsteroidsLoader:
    def __init__(self):
        self.client = bigquery.Client(project=settings.PROJECT_ID)

    def load_data_in_bigquery(self, df, project_id, dataset_id, table_id):

        table = f"{project_id}.{dataset_id}.{table_id}"
        job = self.client.load_table_from_dataframe(df, table)
        job.result()

        print("Loaded", job.output_rows, "rows.")
