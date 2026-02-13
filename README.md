# Task 1 – Name Matching using FAISS

## Overview
This project implements a name-matching system that finds the most similar names
from a predefined dataset using vector similarity search.

Character-level embeddings are used to capture spelling and transliteration
variations in names. FAISS is used to perform efficient cosine similarity search
over the embedded vectors.

This project runs fully locally and does not require any external APIs or paid services.

---

## Project Structure

name-matching/
├── data/
│ └── names_dataset.json
├── embeddings/
│ └── names.index
├── src/
│ ├── init.py
│ ├── data_loader.py
│ ├── embedder.py
│ ├── vector_index.py
│ ├── similarity_search.py
│ └── main.py
├── requirements.txt
├── README.md
└── .gitignore


---

## Setup Instructions

### Requirements
- Python 3.9 or higher
- Windows or Linux
- CPU-only (no GPU required)

---

### Installation

Create and activate a virtual environment (recommended):

```bash
python -m venv env


Windows

env\Scripts\activate


Linux / macOS

source env/bin/activate


Install dependencies:

pip install -r requirements.txt

How to Run

Run the application from the project root directory:

python -m src.main

Usage

When prompted, enter a name to find similar matches:

Enter a name (or type 'exit'): ganesh

Best Match:
ganesh (score: 1.0)

Top Matches:
1. ganesh - 1.0
2. ganesha - 0.8824
3. ganeshan - 0.8055


Only the top 5 matches with a similarity score ≥ 0.4 are returned.