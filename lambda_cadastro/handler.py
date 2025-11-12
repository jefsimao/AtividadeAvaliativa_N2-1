import json
import boto3
import os

sqs = boto3.client('sqs')
QUEUE_URL = os.environ.get('SQS_URL')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(body)
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Cadastro enviado para processamento'})
    }
