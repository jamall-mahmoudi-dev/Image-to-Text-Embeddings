Project Structure and File Descriptions

README.md: Provides an overview of the project, installation instructions, how to run the pipeline, and prerequisites.

requirements.txt: Lists the required Python libraries, including torch, transformers, Pillow, pinecone-client, and tqdm.

config/config.py: Securely stores API keys and image paths.

src/image_captioning.py: Implements the image_to_text(image_path) function using the BLIP model.

src/embeddings.py: Implements the get_image_embedding(image_path) function using the CLIP model.

src/pinecone_utils.py: Contains the save_embedding_to_pinecone(id, embedding, metadata) function and handles connection to Pinecone.

src/pipeline.py: Executes the pipeline concurrently using ThreadPoolExecutor, reads images from the data/ folder, and stores embeddings.

notebooks/test_pipeline.ipynb: Used for testing and experimenting with the pipeline and inspecting embedding results.

scripts/run_pipeline.py: A runnable script to start the pipeline from the terminal with a single command.
# vectorDB on Docker
docker run -p 6333:6333 qdrant/qdrant
