import os
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from config.config import IMAGE_FOLDER
from image_captioning import image_to_text
from embeddings import get_image_embedding
from qdrant_utils import save_embedding_to_qdrant

def process_image(image_path):
    caption = image_to_text(image_path)
    embedding = get_image_embedding(image_path)
    save_embedding_to_qdrant(image_path, embedding, {"caption": caption})
    return image_path, caption

def run_pipeline():
    image_files = [os.path.join(IMAGE_FOLDER, f) for f in os.listdir(IMAGE_FOLDER)]
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(tqdm(executor.map(process_image, image_files), total=len(image_files)))
    print("All images processed!")
    return results
