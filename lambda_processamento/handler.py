import json
import boto3
from utils.db_utils import salvar_no_dynamo

sns = boto3.client('sns')
TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    for record in event['Records']:
        cadastro = json.loads(record['body'])
        salvar_no_dynamo(cadastro)
        
        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=json.dumps({'default': f"Cadastro processado: {cadastro['usuario']}"}),
            MessageStructure='json'
        )
