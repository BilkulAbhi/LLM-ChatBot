from langchain_community.llms import Cohere
chat = Cohere(cohere_api_key="YgzcK00WuBRyeyyMrEYsuhc4U7Gail955W0sTfyc")

from langchain.schema.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="You are Micheal Jordan."),
    HumanMessage(content="Which shoe manufacturer are you associated with?"),
]
response = chat.invoke(messages)
print(response)