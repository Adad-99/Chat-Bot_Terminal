from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

def initialize_chatbot():
    # Carregar variáveis de ambiente
    load_dotenv()

    # Definir personalidade assumida pelo Bot
    template = """
    Você é um programador profissional.
    Responda apenas em Português.

    Input: {input}
    """
    # Cria o template do prompt
    base_prompt = PromptTemplate(input_variables=["input"], template=template)

    # Modelo de linguagem "Groqcloud"
    llm = ChatGroq(model_name="llama3-8b-8192")

    # Configurar a memória da conversa
    memory = ConversationBufferMemory(memory_key="chat_history", input_key='input')

    # Configura a cadeia do modelo LLM
    llm_chain = LLMChain(llm=llm, prompt=base_prompt, memory=memory)

    if llm_chain:
        print("Chatbot inicializado com sucesso.")
    else:
        print("Erro ao inicializar o chatbot.")

    return llm_chain

def generate_response(user_input, llm_chain):
    try:
        response = llm_chain.invoke(input=user_input)
        # Verifica se a resposta é um dicionário e tem o campo 'text'
        if isinstance(response, dict) and 'text' in response:
            return response['text']
        else:
            return "Desculpe, não consegui entender sua pergunta."
        
    except Exception as e:
        response = f"Erro ao processar a resposta: {str(e)}"


# Exemplo de execução para testar a função de resposta
#if __name__ == "__main__":
#    llm_chain = initialize_chatbot()
#    if llm_chain:
#        while True:
#            user_input = input("Você: ")
#            if not user_input:
#                break  # Sai do loop
#
#            # Gerar a resposta usando o modelo de linguagem
#            response = generate_response(user_input, llm_chain)
#            print(f"Assistente: {response}")
