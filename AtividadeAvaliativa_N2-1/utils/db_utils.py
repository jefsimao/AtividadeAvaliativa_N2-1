import boto3
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('DYNAMODB_TABLE')

def salvar_no_dynamo(cadastro):
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item=cadastro)
