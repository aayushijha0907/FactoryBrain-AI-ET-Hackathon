"""
entity_extraction.py

Extract entities from industrial documents for
FactoryBrain AI Knowledge Graph generation.

Supported Entities:
- Equipment
- Documents
- Procedures
- Locations
- Components
- Personnel
"""

import re
from collections import defaultdict


class EntityExtractor:

    def __init__(self):

        self.patterns = {
            "Equipment": [
                r"Pump\s+[A-Za-z0-9]+",
                r"Valve\s+[A-Za-z0-9]+",
                r"Motor\s+[A-Za-z0-9]+",
                r"Boiler\s+[A-Za-z0-9]+",
                r"Compressor\s+[A-Za-z0-9]+",
                r"Generator\s+[A-Za-z0-9]+",
                r"Tank\s+[A-Za-z0-9]+"
            ],

            "Document": [
                r"Maintenance Manual",
                r"Inspection Report",
                r"Safety SOP",
                r"Operating Manual",
                r"Maintenance Report"
            ],

            "Procedure": [
                r"Maintenance",
                r"Inspection",
                r"Calibration",
                r"Shutdown",
                r"Startup"
            ],

            "Location": [
                r"Plant\s+\d+",
                r"Warehouse\s+\d+",
                r"Workshop\s+\d+"
            ],

            "Component": [
                r"Bearing",
                r"Seal",
                r"Filter",
                r"Gasket",
                r"Sensor"
            ],

            "Personnel": [
                r"Technician\s+[A-Za-z]+",
                r"Engineer\s+[A-Za-z]+",
                r"Operator\s+[A-Za-z]+"
            ]
        }

    # ===================================================
    # Extract Entities
    # ===================================================

    def extract_entities(self, text):

        entities = []

        for entity_type, patterns in self.patterns.items():

            for pattern in patterns:

                matches = re.findall(
                    pattern,
                    text,
                    flags=re.IGNORECASE
                )

                for match in matches:

                    entity = {
                        "name": match.strip(),
                        "type": entity_type
                    }

                    if entity not in entities:
                        entities.append(entity)

        return entities

    # ===================================================
    # Group Entities
    # ===================================================

    def group_entities(self, entities):

        grouped = defaultdict(list)

        for entity in entities:
            grouped[entity["type"]].append(
                entity["name"]
            )

        return dict(grouped)

    # ===================================================
    # Count Entities
    # ===================================================

    def count_entities(self, entities):

        counts = {}

        for entity in entities:

            entity_type = entity["type"]

            counts[entity_type] = (
                counts.get(entity_type, 0) + 1
            )

        return counts

    # ===================================================
    # Generate Relationships
    # ===================================================

    def generate_relationships(self, entities):

        relationships = []

        equipment = [
            e["name"]
            for e in entities
            if e["type"] == "Equipment"
        ]

        procedures = [
            e["name"]
            for e in entities
            if e["type"] == "Procedure"
        ]

        for eq in equipment:
            for proc in procedures:

                relationships.append({
                    "source": eq,
                    "target": proc,
                    "relation": "requires"
                })

        return relationships


# ===================================================
# Demo
# ===================================================

if __name__ == "__main__":

    sample_text = """
    Pump A failed during inspection.

    Technician Raj inspected Pump A
    at Plant 2.

    Maintenance Manual recommends
    replacing the Bearing.

    Valve X requires Calibration.

    Engineer Amit approved the
    Maintenance Report.
    """

    extractor = EntityExtractor()

    entities = extractor.extract_entities(
        sample_text
    )

    print("\n===== ENTITIES =====")

    for entity in entities:
        print(entity)

    print("\n===== GROUPED =====")
    print(
        extractor.group_entities(entities)
    )

    print("\n===== COUNTS =====")
    print(
        extractor.count_entities(entities)
    )

    print("\n===== RELATIONSHIPS =====")

    for relation in extractor.generate_relationships(
        entities
    ):
        print(relation)
