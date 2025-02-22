from api.common.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME
)
from pinecone import Pinecone, ServerlessSpec
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Check if the index exists, and create it only if it does not exist
if PINECONE_INDEX_NAME not in pc.list_indexes().names():
    print(f"Creating index: {PINECONE_INDEX_NAME}")
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=384,  # Must match `all-MiniLM-L6-v2`
        metric="cosine",  # Use "euclidean" or "dotproduct" if needed
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
else:
    print(f"Index '{PINECONE_INDEX_NAME}' already exists.")

# Connect to the existing Pinecone index
index = pc.Index(PINECONE_INDEX_NAME)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Pinecone index is ready and model is loaded!")


