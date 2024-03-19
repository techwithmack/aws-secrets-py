import boto3
import json
import os

#create function to get secret
def get_secret(secret_name):
    secret_name = secret_name
    region_name = "us-east-1"

    #cretae a secrets manager client 
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name
    )

    secret = get_secret_value_response['SecretString']
    secret=json.loads(secret)
    for key, value in secret.items():os.environ[key] = value
    #print(os.getenv(secret_name))
    
