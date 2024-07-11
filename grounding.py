import boto3

guardrailId = "ENTER_GUARDRAIL_ID"
guardrailVersion= "ENTER_GUARDRAIL_VERSION"
knowledgeBaseId = "ENTER_KB_ID"

#modelArn = 'arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-text-premier-v1:0'
modelArn = 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-instant-v1'

def main():
    
    client = boto3.client('bedrock-agent-runtime')
    response = client.retrieve_and_generate(
        input={
            'text': 'what is amazon doing in the field of quantum computing?'
        },
        retrieveAndGenerateConfiguration={
            'knowledgeBaseConfiguration': {
                'generationConfiguration': {
                    'guardrailConfiguration': {
                        'guardrailId': guardrailId,
                        'guardrailVersion': guardrailVersion
                    }
                },
                'knowledgeBaseId': knowledgeBaseId,
                'modelArn': modelArn,
                'retrievalConfiguration': {
                    'vectorSearchConfiguration': {
                        'overrideSearchType': 'SEMANTIC'
                    }
                }
            },
            'type': 'KNOWLEDGE_BASE'
        },
    )

    action = response["guardrailAction"]
    print(f'Guardrail action: {action}')
    
    finalResponse = response["output"]["text"]
    print(f'Final response:\n{finalResponse}')

if __name__ == "__main__":
    main()
