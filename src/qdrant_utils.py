from qdrant_client import QdrantClient
from qdrant_client.http import models
from config.config import QDRANT_HOST, QDRANT_PORT, COLLECTION_NAME
import sys
import os

# add sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def get_qdrant_client():
    # timeout increase 
    return QdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT,
        timeout=120  
    )


def create_collection_if_not_exists():
    client = get_qdrant_client()
    collections = client.get_collections().collections
    names = [c.name for c in collections]
    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE)
        )
        print(f"Created collection '{COLLECTION_NAME}'")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")


def insert_embedding(vector, caption):
    client = get_qdrant_client()
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            models.PointStruct(id=1, vector=vector, payload={"caption": caption})
        ],
    )
    print("Embedding inserted successfully.")
