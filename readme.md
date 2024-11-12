# Assistente de Delivery com AWS Step Functions e AWS Bedrock

Este projeto implementa um assistente de delivery automatizado que usa AWS Step Functions para orquestrar o fluxo de trabalho de entrega e AWS Bedrock para responder perguntas dos clientes em linguagem natural. A solução fornece atualizações em tempo real sobre o status do pedido e respostas automatizadas para dúvidas comuns dos clientes.

## Visão Geral do Projeto

O assistente de delivery automatizado é capaz de:

- **Processar pedidos**: Recebe e confirma novos pedidos.
- **Fornecer respostas automáticas**: Utiliza o AWS Bedrock para responder a perguntas frequentes dos clientes.
- **Monitorar o status da entrega**: Verifica o andamento do pedido em várias etapas e atualiza o cliente conforme necessário.
- **Notificar o cliente**: Envia notificações de status via Amazon SNS.

## Arquitetura

### Componentes Principais

1. **AWS Step Functions**: Orquestra o fluxo de trabalho do assistente de delivery.
2. **AWS Bedrock**: Gera respostas automáticas para perguntas frequentes, como "Qual é o status do meu pedido?"
3. **AWS Lambda**: Executa funções para confirmar pedidos, consultar status e enviar respostas.
4. **Amazon DynamoDB**: Armazena informações sobre cada pedido.
5. **Amazon SNS**: Envia notificações ao cliente sobre o status do pedido.

### Diagrama de Fluxo

Receber Pedido -> Confirmar Pedido -> Perguntas do Cliente -> Consultar Status -> Monitorar Entrega -> Notificar Cliente

## Configuração do Projeto

Pré-requisitos

AWS CLI configurado e com permissões adequadas para acessar o AWS Step Functions, Bedrock, Lambda, DynamoDB e SNS.
Python 3.8+ (para desenvolvimento e execução local das funções Lambda, se necessário).

### Configuração do AWS Step Functions

Crie um novo fluxo no Step Functions usando a definição JSON disponível em step_functions_definition.json.
Modifique o ARN das funções Lambda na definição para corresponder ao ARN das funções criadas na sua conta.

### Configuração do AWS Bedrock
No console AWS Bedrock, escolha um modelo pré-treinado, como o Amazon Titan.
Ajuste os parâmetros de resposta para atender aos requisitos do assistente (por exemplo, temperatura = 0.7 e max_tokens = 100).
Modifique a função Lambda ResponderCliente para integrar com o Bedrock e gerar respostas automatizadas.

### Funções Lambda

As funções Lambda incluem:

ConfirmarPedido: Valida o pedido e inicia o processo de entrega.
ConsultarStatus: Consulta o DynamoDB para verificar o status atual do pedido.
MonitorarEntrega: Monitora o progresso do pedido e atualiza seu status.
NotificarCliente: Envia notificações sobre o status e conclusão do pedido via Amazon SNS.
ResponderCliente: Usa o AWS Bedrock para gerar uma resposta personalizada com base na consulta do cliente.

### Banco de Dados - Amazon DynamoDB
Crie uma tabela no DynamoDB para armazenar informações de pedidos com os seguintes campos sugeridos:

PedidoID: Identificador único do pedido.
Status: Status atual do pedido (Ex: "Preparação", "Transporte", "Entregue").
DataCriacao: Data e hora de criação do pedido.

### Notificações - Amazon SNS
Crie um tópico SNS para envio de notificações aos clientes.
Inscreva o número de telefone ou email do cliente para receber as notificações.


## Como Executar
Desenvolvimento e Teste Local:

Testar cada função Lambda individualmente para garantir que as respostas do AWS Bedrock e atualizações do DynamoDB estão funcionando corretamente.

Execução no AWS Step Functions:

Inicie o fluxo de trabalho no Step Functions com dados de entrada para um novo pedido e acompanhe o progresso das etapas.

Validação de Respostas Automáticas:

Simule perguntas frequentes dos clientes, como "Quando meu pedido será entregue?", e verifique se o AWS Bedrock responde de forma adequada e contextualizada.

### Exemplo de Entrada no Step Functions
{
  "PedidoID": "12345",
  "Cliente": {
    "Nome": "João Silva",
    "Telefone": "+5511987654321"
  },
  "pergunta": "Qual é o status do meu pedido?"
}

### Exemplo de resposta do Bedrock
{
  "statusCode": 200,
  "body": {
    "resposta": "Seu pedido está em transporte e deve ser entregue em breve."
  }
}
