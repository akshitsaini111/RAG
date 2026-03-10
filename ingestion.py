import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma #vector database
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Loading documents...")
    # Load documents from the "data" directory
    # Chunk the files into smaller pieces
    # Create embeddings for the chunks
    # Store the embeddings in a vector database
    


if __name__ == "__main__":
    main()

