import sys
import os

# add path sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pipeline import run_pipeline

if __name__ == "__main__":
    image_path = "data/example.jpg"
    run_pipeline(image_path)
