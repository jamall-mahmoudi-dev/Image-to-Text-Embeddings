import pinecone
from config.config import PINECONE_API_KEY

pinecone.init(api_key=PINECONE_API_KEY, environment="us-west1-gcp")
INDEX_NAME = "image-embeddings"
if INDEX_NAME not in pinecone.list_indexes():
    pinecone.create_index(INDEX_NAME, dimension=512)
index = pinecone.Index(INDEX_NAME)

def save_embedding_to_pinecone(id, embedding, metadata=None):
    index.upsert([(id, embedding, metadata or {})])
