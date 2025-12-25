# Code Aware Chunking
from langchain_text_splitters import RecursiveCharacterTextSplitter
code_text = ""  # Define your code text here
code_splitter = RecursiveCharacterTextSplitter.from_language(language="python", chunk_size=1000, chunk_overlap=100)
docs = code_splitter.create_documents([code_text])
