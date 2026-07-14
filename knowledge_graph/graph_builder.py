"""
graph_builder.py
Builds a Knowledge Graph from parsed industrial documents.
Supports entity extraction and relationship detection.
"""

import re
import networkx as nx
from typing import Dict, List, Any, Optional
from datetime import datetime


class KnowledgeGraphBuilder:
    """
    Advanced Knowledge Graph Builder for industrial documents.
    """
    
    def __init__(self):
        self.graph = nx.Graph()
        self.node_counter = 0

    # =====================================================
    # Entity Extraction
    # =====================================================
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """
        Extract different types of entities from document text.
        Ready for future upgrade to SpaCy / LLM-based extraction.
        """
        entities = {
            "Equipment": [],
            "Component": [],
            "Procedure": [],
            "Person": [],
            "Location": [],
            "Measurement": []
        }
        
        # Equipment patterns
        patterns = {
            "Equipment": [
                r"Pump\s?[A-Z0-9-]+", r"Valve\s?[A-Z0-9-]+", r"Compressor\s?[A-Z0-9-]+",
                r"Boiler\s?[A-Z0-9-]+", r"Generator\s?[A-Z0-9-]+", r"Motor\s?[A-Z0-9-]+",
                r"Tank\s?[A-Z0-9-]+", r"Turbine\s?[A-Z0-9-]+"
            ],
            "Component": [
                r"bearing", r"seal", r"filter", r"gasket", r"impeller", r"shaft", 
                r"rotor", r"stator", r"pipe", r"flange"
            ],
            "Procedure": [
                r"SOP", r"maintenance procedure", r"inspection protocol", 
                r"calibration", r"shutdown", r"startup"
            ],
            "Person": [
                r"Technician [A-Z][a-z]+", r"Engineer [A-Z][a-z]+", 
                r"Operator [A-Z][a-z]+"
            ],
            "Measurement": [
                r"\d+\.?\d*\s*(bar|psi|°C|°F|rpm|hours|days|weeks)"
            ]
        }
        
        for entity_type, regex_list in patterns.items():
            for pattern in regex_list:
                matches = re.findall(pattern, text, flags=re.IGNORECASE)
                for match in matches:
                    cleaned = match.strip()
                    if cleaned and cleaned not in entities[entity_type]:
                        entities[entity_type].append(cleaned)
        
        return {k: v for k, v in entities.items() if v}

    # =====================================================
    # Graph Construction
    # =====================================================
    def build_graph(self, document: Dict[str, Any]) -> nx.Graph:
        """
        Build knowledge graph from a parsed document.
        """
        filename = document["filename"]
        text = document.get("text", "")
        
        # Add document node
        self.graph.add_node(
            filename,
            node_type="Document",
            pages=document.get("pages", 1),
            added_at=datetime.now().isoformat()
        )
        
        # Extract entities
        entities = self.extract_entities(text)
        
        # Add entities and relationships
        for entity_type, items in entities.items():
            for item in items:
                # Add entity node
                self.graph.add_node(
                    item,
                    node_type=entity_type,
                    added_at=datetime.now().isoformat()
                )
                
                # Add edge between document and entity
                self.graph.add_edge(
                    filename,
                    item,
                    relation="mentions",
                    weight=1.0
                )
        
        return self.graph

    # =====================================================
    # Utilities
    # =====================================================
    def get_statistics(self) -> Dict[str, Any]:
        """Return graph statistics."""
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "density": round(nx.density(self.graph), 4),
            "connected_components": nx.number_connected_components(self.graph),
            "average_degree": round(sum(dict(self.graph.degree()).values()) / self.graph.number_of_nodes(), 2) 
                              if self.graph.number_of_nodes() > 0 else 0
        }

    def get_graph(self) -> nx.Graph:
        return self.graph

    def clear(self):
        """Reset the graph."""
        self.graph.clear()
        self.node_counter = 0

    def add_relationship(self, source: str, target: str, relation: str, weight: float = 1.0):
        """Manually add a custom relationship."""
        self.graph.add_edge(source, target, relation=relation, weight=weight)


# =====================================================
# Demo / Testing
# =====================================================
if __name__ == "__main__":
    sample_document = {
        "filename": "maintenance_manual_v2.pdf",
        "pages": 42,
        "text": """
        Pump A was inspected yesterday by Technician Raj.
        Valve X showed signs of leakage at 12.5 bar pressure.
        Compressor C requires urgent maintenance.
        Boiler B should be checked weekly according to Safety SOP.
        The impeller in Pump A needs replacement.
        """
    }

    builder = KnowledgeGraphBuilder()
    graph = builder.build_graph(sample_document)

    print("✅ Knowledge Graph Built Successfully!\n")
    print(f"Nodes : {graph.number_of_nodes()}")
    print(f"Edges : {graph.number_of_edges()}\n")
    
    print("Nodes with attributes:")
    for node, data in graph.nodes(data=True):
        print(f"  • {node} ({data.get('node_type', 'Unknown')})")
    
    print("\nRelationships:")
    for u, v, data in graph.edges(data=True):
        print(f"  • {u} --[{data.get('relation', 'related')}]--> {v}")
    
    print("\nStatistics:")
    print(builder.get_statistics())
