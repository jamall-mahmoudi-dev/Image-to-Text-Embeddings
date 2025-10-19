from src.image_captioning import generate_caption
from src.embeddings import get_text_embedding
from src.qdrant_utils import create_collection_if_not_exists, insert_embedding

def run_pipeline(image_path: str):
    print(" Starting pipeline...")

    caption = generate_caption(image_path)
    print(f" Generated caption: {caption}")

    embedding = get_text_embedding(caption)
    print(f" Embedding length: {len(embedding)}")

    create_collection_if_not_exists()
    insert_embedding(embedding, caption)

    print(" Pipeline completed successfully.")
