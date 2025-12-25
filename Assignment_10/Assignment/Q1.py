# Basic Fixed-Size Chunking

from langchain_text_splitters import CharacterTextSplitter

raw_text = ""  # Add your text content here
text_splitter = CharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = text_splitter.create_documents ([raw_text])
# Note : Simple , but can split sentences unexpectedly 