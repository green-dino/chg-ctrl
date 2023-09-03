import networkx as nx
import plotly.graph_objects as go
import tkinter as tk
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define your relationships
relationships = {
    'User': {'initiates': ['Work Role'], 'selects': ['Role Selected']},
    'Work Role': {'addresses': ['Problem'], 'initiates': ['Change', 'Request']},
    'Problem': {'links_to': ['Change Control Record']},
    'Change': {'links_to': ['Change Control Record'], 'conducts': ['Evaluation']},
    'Request': {'links_to': ['Change Control Record'], 'initiates': ['Fulfillment']},
    'Change Control Record': {'captures': ['Document Control Information', 'Change Implementation Plan'],
                              'determines': ['Communication and Notification'],
                              'assesses': ['Risk Assessment and Control'],
                              'references': ['Document References']},
    'Framework': {'incorporates': ['Loops', 'Functions']},
    'Playbooks': {'maps': ['Mappings', 'Roles']},
    'Role Selected': {'manages': ['Trouble Tickets']},
    'Trouble Tickets': {'provides': ['View']}
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for from_entity, actions in relationships.items():
    for action, to_entities in actions.items():
        for to_entity in to_entities:
            G.add_edge(from_entity, to_entity, relationship=action)

# Create the main GUI window
root = tk.Tk()
root.title("Relationship Visualizer")

# Create a canvas for displaying the graph
canvas = FigureCanvasTkAgg(plt.figure(figsize=(8, 8)))
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Function to draw and display the graph using Plotly
def draw_graph():
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'relationship')

    # Create a Plotly subplot
    fig = make_subplots(rows=1, cols=1)
    
    # Add nodes to the Plotly subplot
    for node in G.nodes:
        fig.add_trace(go.Scatter(x=[pos[node][0]], y=[pos[node][1]], text=node, mode="markers+text"))

    # Add edges to the Plotly subplot
    edge_x = []
    edge_y = []
    for edge in G.edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    fig.add_trace(go.Scatter(x=edge_x, y=edge_y, line=dict(width=1, color='gray'), mode='lines'))

    # Set axis properties
    fig.update_xaxes(showticklabels=False, showgrid=False)
    fig.update_yaxes(showticklabels=False, showgrid=False)

    # Add labels for edges
    for edge, label in labels.items():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        fig.add_annotation(
            x=(x0 + x1) / 2, y=(y0 + y1) / 2,
            text=label,
            showarrow=False,
            font=dict(color='red')
        )

    # Update layout properties
    fig.update_layout(
        title="Relationship Graph",
        title_x=0.5,
        autosize=True,
        margin=dict(l=0, r=0, b=0, t=0)
    )

    fig.show()

# Button to redraw and display the graph
draw_button = tk.Button(root, text="Draw Graph", command=draw_graph)
draw_button.pack()

# Run the initial drawing
draw_graph()

# Start the GUI main loop
root.mainloop()
