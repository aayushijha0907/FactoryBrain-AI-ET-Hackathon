"""
constants.py

Stores application-wide constants.
"""

# =====================================
# APP
# =====================================

APP_TITLE = "FactoryBrain AI"

TAGLINE = (
    "Transforming Industrial Knowledge "
    "into Actionable Intelligence"
)

# =====================================
# SIDEBAR
# =====================================

SIDEBAR_OPTIONS = [
    "🏠 Home",
    "📤 Upload Documents",
    "💬 AI Chat",
    "📊 Dashboard",
    "🕸️ Knowledge Graph"
]

# =====================================
# ENTITY TYPES
# =====================================

ENTITY_TYPES = [
    "Equipment",
    "Document",
    "Procedure",
    "Location",
    "Personnel",
    "Component",
    "Insight"
]

# =====================================
# COLORS
# =====================================

NODE_COLORS = {
    "Equipment": "#10B981",
    "Document": "#4F46E5",
    "Procedure": "#F59E0B",
    "Location": "#06B6D4",
    "Personnel": "#EF4444",
    "Component": "#14B8A6",
    "Insight": "#8B5CF6"
}

# =====================================
# DEFAULT VALUES
# =====================================

DEFAULT_CHUNK_SIZE = 500

DEFAULT_CHUNK_OVERLAP = 50

DEFAULT_QUERY_RESULTS = 5
