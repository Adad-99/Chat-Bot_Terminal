from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

def chat_bot():
    #.env
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

    # Configurar a cadeia do modelo LLM
    llm_chain = LLMChain(llm=llm, prompt=base_prompt, memory=memory)

    # Limpar o terminal
    os.system("cls")

    while True:

        user_input = input("Você: ")        
        if not user_input:
            break  # Sai do loop
        
        # Gerar a resposta usando o modelo de linguagem
        response = llm_chain.run(input=user_input)
        print(f"Assistente: {response}")
