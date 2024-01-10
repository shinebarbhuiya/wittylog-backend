import requests
from langchain.text_splitter import RecursiveCharacterTextSplitter

"""
Using langchain here because I might end up using it for more things in future.
"""


def create_vector_from_content(text: str):
   
    url = "https://api.deepinfra.com/v1/inference/BAAI/bge-large-en-v1.5"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer cWdwwQiCJIL6SoODOcHMYAyW5S99InVF"
    }

    data = {"inputs": [text]}
    
    response = requests.post(url, json=data, headers=headers)
    data = response.json()['embeddings'][0]

    return data


def split_texts(text: str):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    texts = text_splitter.split_text(text)

    return texts 

    # You can use for loop to get text chunks from this 'texts'

