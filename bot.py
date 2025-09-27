from langchain_huggingface import HuggingFaceEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from db.config import rev_embeddings_collection
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

vector_store = MongoDBAtlasVectorSearch(
    collection=rev_embeddings_collection,
    embedding=embeddings,
    embedding_key="embeddings",
    relevance_score_fn="cosine",
    index_name="REVIEW_VECTOR_INDEX"
)

def ask(query: str):
    retrieved_docs = vector_store.similarity_search(query=query, k=3)
    context = '\n\n'.join([doc.page_content for doc in retrieved_docs])
    prompt = f"""
    You are a helpful Assistant who helps people to:
    - Helps people to guide about their career
    - Helps people to detect red flags in an internship, copy pasted from description or told in a question
    - Helps people to suggest advice related to finding internships

    Rules:
    - If someone asks query about detecting red flags or query related to joining in an internship, Use the following context provided from the knowledge base and apply:
    {context}

    - If someone asks query about guidance / mentorship related to career, your job is to guide them in a warm soft manner like a friend
    Remember you are a hope for someone who is desperate and need to advance his career or get jobs.

    The question is given below:
    {query}
    """
    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content" : prompt},
            {"role": "user", "content": query}
        ],
        temperature=0.5,
        model="llama-3.1-8b-instant"
        )
    return response.choices[0].message.content
