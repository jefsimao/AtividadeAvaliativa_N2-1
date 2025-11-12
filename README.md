# 🔄 Sistema de Cadastro de Trocas com AWS (Python + JSON)

Este projeto implementa uma arquitetura serverless utilizando serviços da AWS para gerenciar cadastros de trocas de forma escalável, assíncrona e monitorada. A aplicação é escrita em Python e utiliza JSON para comunicação entre os componentes.

---

## 🧱 Arquitetura

A solução é baseada em uma arquitetura orientada a eventos com os seguintes componentes:

- **API Gateway**: Recebe requisições HTTP dos usuários.
- **Lambda - Cadastro de Troca**: Processa a entrada do usuário e envia para a fila SQS.
- **Amazon SQS**: Armazena cadastros de troca para processamento assíncrono.
- **Lambda - Processamento Assíncrono**: Consome mensagens da fila, grava no banco de dados e envia notificações.
- **Amazon DynamoDB**: Armazena os cadastros para reutilização.
- **Amazon SNS**: Envia notificações ao usuário após o processamento.
- **Amazon CloudWatch**: Monitora logs e métricas das funções Lambda.

---

## 📁 Estrutura do Projeto

```plaintext
troca-cadastro/
├── lambda_cadastro/
│   ├── handler.py
│   └── event_sample.json
├── lambda_processamento/
│   ├── handler.py
│   └── event_sample.json
├── utils/
│   └── db_utils.py
├── templates/
│   └── notification_template.json
├── requirements.txt
└── README.md
🚀 Como Executar Localmente
Instale dependências:

bash
pip install -r requirements.txt
Configure suas credenciais AWS:

bash
aws configure
Teste local com AWS SAM:

bash
sam local invoke CadastroFunction --event lambda_cadastro/event_sample.json
sam local invoke ProcessamentoFunction --event lambda_processamento/event_sample.json
⚙️ Variáveis de Ambiente
Configure as seguintes variáveis nas funções Lambda:

SQS_URL: URL da fila SQS.

SNS_TOPIC_ARN: ARN do tópico SNS.

DYNAMODB_TABLE: Nome da tabela DynamoDB.

📤 Implantação com AWS SAM
Crie um template.yaml para empacotar e implantar os recursos:

bash
sam build
sam deploy --guided
📊 Monitoramento
Utilize o Amazon CloudWatch para:

Visualizar logs das funções Lambda.

Criar métricas customizadas.

Configurar alarmes para falhas ou lentidão.

📬 Notificações
O SNS envia notificações com base no modelo definido em templates/notification_template.json. Você pode personalizar mensagens para e-mail, SMS ou outros protocolos suportados.

🛡️ Segurança
As funções Lambda devem ter permissões mínimas necessárias (principle of least privilege).

Use políticas IAM específicas para acesso ao SQS, SNS e DynamoDB.

