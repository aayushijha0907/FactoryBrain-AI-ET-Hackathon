import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def create_sample_knowledge_graph():
    """Create a richer sample industrial knowledge graph."""
    G = nx.Graph()
    
    # Nodes with attributes
    nodes = {
        "Pump A": {"type": "Equipment", "color": "#1E88E5"},
        "Valve X": {"type": "Equipment", "color": "#1E88E5"},
        "Boiler 3": {"type": "Equipment", "color": "#1E88E5"},
        
        "Maintenance Report": {"type": "Document", "color": "#43A047"},
        "Inspection Report Q2": {"type": "Document", "color": "#43A047"},
        "Safety SOP": {"type": "Procedure", "color": "#FB8C00"},
        
        "Technician Raj": {"type": "Person", "color": "#8E24AA"},
        "Failure Analysis": {"type": "Insight", "color": "#E53935"},
    }
    
    for node, data in nodes.items():
        G.add_node(node, **data)
    
    # Relationships
    edges = [
        ("Pump A", "Maintenance Report"),
        ("Pump A", "Inspection Report Q2"),
        ("Pump A", "Safety SOP"),
        ("Pump A", "Failure Analysis"),
        ("Valve X", "Inspection Report Q2"),
        ("Boiler 3", "Safety SOP"),
        ("Technician Raj", "Maintenance Report"),
        ("Technician Raj", "Inspection Report Q2"),
        ("Failure Analysis", "Pump A"),
    ]
    
    G.add_edges_from(edges)
    return G


def show_graph():
    st.markdown(
        """
        <h1 style='text-align:center; color:#1E3A8A;'>
            🕸️ Industrial Knowledge Graph
        </h1>
        <p style='text-align:center; color:#64748b;'>
            Visualize relationships between equipment, documents, procedures, and insights
        </p>
        """,
        unsafe_allow_html=True
    )
    
    st.divider()

    # Controls
    col1, col2 = st.columns([3, 1])
    with col1:
        graph_mode = st.radio(
            "Graph View",
            options=["Interactive Preview", "Full Network"],
            horizontal=True
        )
    
    with col2:
        if st.button("🔄 Regenerate Graph"):
            st.rerun()

    st.divider()

    # Generate Graph
    G = create_sample_knowledge_graph()

    # Draw Graph
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Layout
    pos = nx.spring_layout(G, seed=42, k=0.8)
    
    # Node colors
    node_colors = [G.nodes[node]['color'] for node in G.nodes()]
    
    # Draw nodes
    nx.draw_networkx_nodes(
        G, pos,
        node_color=node_colors,
        node_size=2800,
        alpha=0.9,
        edgecolors="white",
        linewidths=2,
        ax=ax
    )
    
    # Draw edges
    nx.draw_networkx_edges(
        G, pos,
        width=2.5,
        alpha=0.7,
        edge_color="#78909C",
        ax=ax
    )
    
    # Draw labels
    nx.draw_networkx_labels(
        G, pos,
        font_size=9,
        font_weight="bold",
        font_color="white",
        ax=ax
    )
    
    ax.set_axis_off()
    plt.title("FactoryBrain AI - Knowledge Graph", fontsize=16, pad=20)
    
    st.pyplot(fig, use_container_width=True)

    st.divider()

    # Statistics
    st.subheader("📊 Graph Statistics")
    
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    with stats_col1:
        st.metric("Nodes", G.number_of_nodes())
    with stats_col2:
        st.metric("Edges", G.number_of_edges())
    with stats_col3:
        st.metric("Connected Components", nx.number_connected_components(G))
    with stats_col4:
        st.metric("Density", f"{nx.density(G):.3f}")

    st.divider()

    # Node Legend
    st.subheader("🔖 Node Types Legend")
    legend = {
        "🔧 Equipment": "#1E88E5",
        "📄 Document": "#43A047",
        "📜 Procedure": "#FB8C00",
        "👤 Person": "#8E24AA",
        "💡 Insight": "#E53935"
    }
    
    cols = st.columns(len(legend))
    for col, (label, color) in zip(cols, legend.items()):
        with col:
            st.markdown(
                f"<div style='background:{color}; color:white; padding:10px; "
                f"border-radius:8px; text-align:center; font-weight:bold;'>"
                f"{label}</div>",
                unsafe_allow_html=True
            )

    st.divider()

    # Future Vision
    st.info(
        """
        **🔮 Future Capabilities (Post-Hackathon):**
        - Automatic entity extraction from documents
        - Real-time relationship detection using LLM
        - Interactive graph exploration (click nodes)
        - Temporal knowledge (version history)
        - Integration with maintenance systems
        """
    )

    st.caption("FactoryBrain AI • Knowledge Graph Visualization • ET Hackathon 2026")
