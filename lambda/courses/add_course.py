import boto3
import json
import os
dynamodb = boto3.resource('dynamodb')
table_name=os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def add(event, context):
    try:
        table.put_item(Item=event)
        resp = {
            'statusCode': 200,
            'message': 'course details added successfully'
        }
        return json.dumps(resp)
    except Exception as e:
        response = {
            'statusCode': 500,
            'message': 'course details not found'
        }
        raise Exception(json.dumps(response))
