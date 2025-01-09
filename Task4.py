# TASK 4 : 

# Large Language Model & LangChain :

# 1. Use LangChain to:
#     - Load a text file or dataset and split it into chunks.
#     - Create a simple chatbot using the text as a knowledge base (use OpenAI GPT-3.5 or another model).

# 2. Demonstrate how to query a Large Language Model for summarization or question-answering.



# import modules

import os
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
# from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
from openai import api_key

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY") #apply openai key


PINECONE_API_KEY=os.getenv("PINECONE_API_KEY") #apply pinecone key


#function

def retrieve_information_fromTEXT(text_path: str, query: str, index_name: str = "test"):
    try:
        # Initialize OpenAI embeddings and txt loader
        embeddings = OpenAIEmbeddings()
        loader = TextLoader(text_path)

        # Load documents and split them into chunks
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)

        # Create Pinecone vector store from documents
        vectorstore = PineconeVectorStore.from_documents(
            docs,
            index_name=index_name,
            embedding=embeddings
        )

        # Initialize the language model and setup RetrievalQA
        llm = ChatOpenAI(model_name='gpt-3.5-turbo')
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )

        # Get response for the query
        response = qa.invoke(query)

        return response["result"]

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Example usage
text_path = "C:/Users/girdh/Desktop/Assignment/Bhagat Singh.txt"
query = input("Type your Query : ") # query from user


##call the function 
response = retrieve_information_fromTEXT(text_path, query)
print() #use for space
print(response)

