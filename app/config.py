"""
config.py

Application configuration settings.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# =====================================
# APP CONFIGURATION
# =====================================

APP_NAME = "FactoryBrain AI"
APP_VERSION = "1.0.0"

# =====================================
# GEMINI
# =====================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

# =====================================
# FILES
# =====================================

UPLOAD_FOLDER = "uploads"

SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".txt",
    ".png",
    ".jpg",
    ".jpeg"
]

MAX_FILE_SIZE_MB = 25

# =====================================
# CHROMADB
# =====================================

CHROMA_COLLECTION_NAME = (
    "factorybrain"
)

# =====================================
# KNOWLEDGE GRAPH
# =====================================

GRAPH_OUTPUT_FILE = (
    "assets/knowledge_graph.html"
)

# =====================================
# LOGGING
# =====================================

LOG_FILE = (
    "logs/factorybrain.log"
)

# =====================================
# DOCUMENT CHUNKING
# =====================================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 50

# =====================================
# STREAMLIT
# =====================================

PAGE_TITLE = "FactoryBrain AI"

PAGE_ICON = "🏭"

LAYOUT = "wide"
