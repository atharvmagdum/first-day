# Recursive Character Chunking 
from langchain_text_splitters import CharacterTextSplitter

raw_text = ""  # Define your text here
text_splitter = CharacterTextSplitter(chunk_size = 800, chunk_overlap = 100, separators = ["\n\n", "\n", " ", " "])
docs = text_splitter.create_documents([raw_text])
