from openai import AzureOpenAI
from env import config
from utils.logging_utils import setup_logging
import logging

setup_logging(console=False)

client = AzureOpenAI(
    api_key=config.AZURE_OPENAI_API_KEY,
    api_version=config.AZURE_OPENAI_API_VERSION,
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that provides clear and concise answers to technical questions."
    },
    {
        "role": "user",
        "content": "What is the difference between Azure Blob Storage and Azure Data Lake Storage?"
    }
]

response = client.chat.completions.create(
    model=config.AZURE_OPENAI_DEPLOYMENT,
    messages=messages
)

logging.info(f"MESSAGE_SENT: {messages}")
logging.info(f"RESPONSE_RECEIVED: {response.model_dump()}")

print(response.choices[0].message.content)
