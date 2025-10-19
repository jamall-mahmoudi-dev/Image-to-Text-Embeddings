from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams
from config.config import QDRANT_URL, QDRANT_API_KEY

# connections 
client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

COLLECTION_NAME = "image_embeddings"

# create  collection if Not existe
if COLLECTION_NAME not in client.get_collections().collections:
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=512, distance="Cosine")  # CLIP embedding size
    )

def save_embedding_to_qdrant(id, embedding, metadata=None):
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[{
            "id": id,
            "vector": embedding.tolist(),
            "payload": metadata or {}
        }]
    )

def search_embedding(query_embedding, top_k=5):
    result = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding.tolist(),
        top=top_k
    )
    return result
