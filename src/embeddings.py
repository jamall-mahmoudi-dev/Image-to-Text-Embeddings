from sentence_transformers import SentenceTransformer
# get all git
#new change file
def get_text_embedding(text: str):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embedding = model.encode(text)
    return embedding.tolist()