from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List

'''
this function convets text into embeddings to store in Vector DB
'''
def create_faiss_index(texts: List[str]):
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-mpnet-base-v2"
    )
    return FAISS.from_texts(texts, embeddings)
    """
    FAISS.from_texts()
    1. this take the texts as input.
    2. Converts them into vectors using embeddings and store the vectors in FAISS database.
    """

'''
Writing a function to retrive the data from vector DB.
'''

def retrieve_relavant_docs(vectorstore: FAISS, query=str, k:int=4):
    return vectorstore.similarity_search(query,k=k)


    
