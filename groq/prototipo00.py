# from dotenv import load_dotenv

# from langchain_core.messages import SystemMessage,HumanMessage
# import os
# import asyncio
# from groq import AsyncGroq

# load_dotenv()

# client = AsyncGroq(
#     # This is the default and can be omitted
#     api_key=os.environ.get("api"),
# )


# async def main() -> None:
#     chat_completion = await client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": input("Você:"),
#             }
#         ],
#         model="llama3-8b-8192",
#     )
#     print(chat_completion.choices[0].message.content)


# asyncio.run(main())

# from dotenv import load_dotenv
# from langchain_core.messages import SystemMessage, HumanMessage
# import os
# from langchain_groq import ChatGroq
# from langchain_core.output_parsers import StrOutputParser

# # Carrega as variáveis do arquivo .env
# load_dotenv()

# # Configura o cliente Groq e passa a chave da API
# llm = ChatGroq(
#     model="mixtral-8x7b-32768",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     api_key=os.environ.get("api"),  # Passa a chave de API aqui também
# )

# # Captura a entrada do usuário
# user_input = input("Você: ")

# # Define as mensagens com SystemMessage e HumanMessage
# messages = [
#     SystemMessage(content="Você é um assistente que irá responder tudo em português."),
#     HumanMessage(content=user_input)  # A entrada do usuário é passada aqui
# ]

# # Cria o parser para a saída de texto
# parser = StrOutputParser()

# # Cria a cadeia de execução (pipeline) com o modelo e o parser
# chain = llm | parser

# # Invoca a cadeia de execução passando as mensagens
# # Passa a lista de mensagens (não mais um dicionário)
# texto = chain.invoke(messages)

# # Exibe a resposta do modelo
# print(f"Assistente: {texto}")

#-------------------COM ASYNC

import os
import asyncio
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis do arquivo .env
load_dotenv()

# Função assíncrona principal
async def main():
    # Configura o cliente Groq e passa a chave da API
    llm = ChatGroq(
        model="mixtral-8x7b-32768",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ.get("api"),  # Passa a chave de API aqui também
    )

    # Captura a entrada do usuário
    user_input = input("Você: ")

    # Define as mensagens com SystemMessage e HumanMessage
    messages = [
        SystemMessage(content="Você é um assistente que irá responder tudo em português."),
        HumanMessage(content=user_input)  # A entrada do usuário é passada aqui
    ]

    # Cria o parser para a saída de texto
    parser = StrOutputParser()

    # Cria a cadeia de execução (pipeline) com o modelo e o parser
    chain = llm | parser

    # Invoca a cadeia de execução passando as mensagens de forma síncrona
    texto = chain.invoke(messages)

    # Exibe a resposta do modelo
    print(f"Assistente: {texto}")

# Executa a função principal assíncrona
asyncio.run(main())
