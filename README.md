**ChatBot com LangChain e Groq**
    Este projeto implementa um chatbot utilizando a biblioteca LangChain e o modelo de linguagem Groq para fornecer respostas em português, assumindo o papel de um programador profissional.

**Funcionalidades**
    O bot utiliza um template de prompt para gerar respostas contextuais baseadas no input do usuário.
    Mantém uma memória da conversa utilizando o ConversationBufferMemory.
    Usa o modelo llama3-8b-8192 da Groq para gerar respostas.
    O bot é configurado para responder apenas em português.

**Requisitos**
    Python 3.8 ou superior
    Instalar as dependências necessárias com o pip
    Conta ou acesso à API do modelo Groq

Para executar o chatbot, rode o script main.py:
O chatbot estará pronto para receber entradas do usuário e responder em português, mantendo o contexto da conversa.

Dependências
LangChain
GroqCloud
dotenv

**Exemplo de Uso**
Você: Olá, qual é a melhor prática para inicializar um projeto Python?
Assistente: A melhor prática para iniciar um projeto Python é criar um ambiente virtual com `venv`, configurar um arquivo `requirements.txt` e organizar o código em módulos.


