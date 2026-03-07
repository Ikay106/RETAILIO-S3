import os
import boto3
import pandas as pd
import awswrangler as wr
from dotenv import load_dotenv

load_dotenv()

access = os.getenv('ACCESS_KEY')
secret = os.getenv('SECRET_KEY')
region = os.getenv('REGION')
bucket = "retailio-data-lake-ik"

session = boto3.Session(
    aws_access_key_id = access,
    aws_secret_access_key = secret,
    region_name = region
    )

dataset = {
    "products":"data/products.csv",
    "customers": "data/customers.csv",
    "sales": "data/sales.csv"
}

for name,path in dataset.items():
    if os.path.exists(path):
        df = pd.read_csv(path, encoding='latin1')
        wr.s3.to_parquet(
            df = df,
            path =f"s3://{bucket}/raw/{name}",
            index = False,
            mode = 'overwrite',
            dataset = True,
            boto3_session= session
        )
    else:
        print(f"{path} does not exist")