import os
import boto3
import panadas as pd
import awswrangler as wr
from dotenv import load_dotenv

load_dotenv()

access = os.getenv('ACCESS_key')
secret = os.getenv('SECRET_KEY')
regio = os.getenv('REGON')