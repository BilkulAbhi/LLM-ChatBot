from langchain_cohere.llms import Cohere
import os



llm = Cohere(cohere_api_key="FSnVzB20HKHMMGSoTvjCbIw6Kt8MegvM7vIUuErF")

response = llm.invoke("List the seven wonders of the world.")
print(response)