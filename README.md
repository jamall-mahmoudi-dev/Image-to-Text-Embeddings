#  Image-to-Text Embeddings Pipeline

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-green)](https://qdrant.tech/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

A **robust pipeline** to convert images into **text captions** and **vector embeddings**, stored in a **vector database (Qdrant)** for fast similarity search, AI recommendations, or semantic retrieval.

---

##  Project Goal

This project allows you to:

- Automatically generate **descriptive captions** for images using the **BLIP model**.
- Generate **vector embeddings** of images using **CLIP** for semantic similarity.
- Store and query embeddings in a **vector database** (Qdrant) efficiently.
- Enable downstream tasks like **image search, clustering, or recommendation systems**.

---
```
##  Project Structure


Image-to-Text-Embeddings/
├─ README.md # Project overview and instructions
├─ requirements.txt # Python dependencies
├─ config/
│ └─ config.py # API keys, Qdrant config
├─ src/
│ ├─ image_captioning.py # image_to_text(image_path) using BLIP
│ ├─ embeddings.py # get_image_embedding(image_path) using CLIP
│ ├─ pipeline.py # Executes pipeline for all images
│ ├─ qdrant_utils.py # Qdrant client, create collection, insert embeddings
│ └─ pinecone_utils.py # (Optional) Pinecone integration
├─ scripts/
│ └─ run_pipeline.py # Launch pipeline from terminal
└─ notebooks/
└─ test_pipeline.ipynb # Testing and experimenting with embeddings
```
...................................................................

##  Prerequisites

- Python 3.10+  
- Docker (for running Qdrant locally)  
- Install dependencies:

```
pip install -r requirements.txt

docker run -p 6333:6333 qdrant/qdrant
```
 How to Run

Place your images in the data/ folder.
```
Configure Qdrant in config/config.py:
QDRANT_HOST = "127.0.0.1"
QDRANT_PORT = 6333
COLLECTION_NAME = "image_embeddings"
Run the pipeline:
python -m scripts.run_pipeline
```
```
Check output:
Generated caption: <span style="color: #00cc66;">a white Nissan SUV with a black rim</span>
Embedding length: 384
Collection 'image_embeddings' already exists.
Embedding inserted successfully.
Pipeline completed successfully.
```
```
 Workflow Diagram
 flowchart LR
    A[Images in data/] --> B[BLIP Model]
    B --> C[Text Captions]
    A --> D[CLIP Model]
    D --> E[Vector Embeddings]
    C & E --> F[Qdrant VectorDB]
    F --> G[Semantic Search / Recommendations]
```
 Key Features

BLIP: Generates high-quality captions.

CLIP embeddings: Provides 384-dimensional vector representations.

Qdrant integration: Fast and scalable similarity search.

Threaded pipeline: Efficient batch processing of large image datasets.

Optional Pinecone support for cloud vector storage.

 Notes::

Use use_fast=True for BLIP for faster processing.

For large models, allow full download before running pipeline to avoid timeout.

Pipeline is fully extensible for additional models or vector DBs.

 References

BLIP Model (Salesforce)

CLIP Model (OpenAI)

Qdrant Vector Database

...............................................
🔹 How It Works

This project provides an automated pipeline to convert images into text captions and vector embeddings:

Captioning:

Each image is processed using the BLIP model, generating a short and accurate textual description.

Example: For an image of a car, the output might be "a white Nissan SUV with a black rim".

Embedding:

The image or its caption is converted into a 384-dimensional vector using the CLIP model.

This vector represents the semantic meaning of the image in a high-dimensional space and can be used for similarity comparisons or searches.

Storing in a Vector Database:

Generated vectors are stored in Qdrant.

Qdrant enables fast retrieval and similarity search for images based on their semantic content.

Batch & Automated Pipeline:

Multiple images can be processed concurrently using ThreadPoolExecutor.

Outputs include the generated captions, embeddings, and confirmation of successful insertion into Qdrant.

```
🔹 Main Goals

Automatically generate text captions for images.

Create high-quality embeddings for AI applications.

Store and manage vectors in a scalable VectorDB.

Provide a simple and ready-to-use pipeline for various AI/ML projects.
```
🔹 Use Cases

This project can be used for:

Semantic Image Search:

Find images that are semantically similar to a given example.

Recommendation Systems:

Suggest products, clothing, cars, etc., based on visual similarity.

Clustering & Categorization:

Group similar images for content management or data analysis.

AI-powered Business Insights:

Extract insights from images, such as inventory analysis, product review, or market analysis.

Research & Academic Projects:

Study semantic similarity, embeddings, and vector search on image datasets.