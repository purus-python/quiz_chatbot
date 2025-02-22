from common.config import AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, ANTHROPIC_VERSION, MODEL_ID, SERVICE_NAME

import boto3, json

from botocore.config import Config

def bedrock_methods(prompt,output_tokens):
    config = Config(read_timeout=2000)
    bedrock_client = boto3.client(
            service_name=SERVICE_NAME,
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            config=config
        )
    body = {
        "max_tokens":output_tokens,
        "anthropic_version": ANTHROPIC_VERSION,
        "temperature": 0.1,
        "top_p": 0.9,
        "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        
    }
    modelId = MODEL_ID
    accept = 'application/json'
    contentType = 'application/json'
    response = bedrock_client.invoke_model(body=json.dumps(body), modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    completion_text = response_body['content'][0]['text']
    return completion_text