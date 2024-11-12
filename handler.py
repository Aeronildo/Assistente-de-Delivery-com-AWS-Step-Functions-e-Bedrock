import boto3
import json

# Cliente do Bedrock
bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    # Receber a pergunta do cliente
    pergunta_cliente = event.get('pergunta', 'Qual é o status do meu pedido?')

    # Configuração do input para o modelo
    bedrock_input = {
        "prompt": f"{pergunta_cliente}",
        "max_tokens": 100,
        "temperature": 0.7,
        "top_p": 0.9,
    }
    
    # Chamada ao modelo Bedrock (substitua 'nome-do-modelo' pelo modelo apropriado)
    response = bedrock_client.invoke_model(
        modelId="nome-do-modelo",  # Substitua com o ID do modelo Bedrock desejado
        contentType="application/json",
        accept="application/json",
        body=json.dumps(bedrock_input)
    )
    
    # Processamento da resposta
    response_body = json.loads(response['body'].read())
    resposta = response_body.get('generated_text', 'Desculpe, não consegui responder à sua pergunta no momento.')

    return {
        'statusCode': 200,
        'body': json.dumps({
            'resposta': resposta
        })
    }
