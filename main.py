import matplotlib.pyplot as plt
import networkx as nx

# Initialize a directed graph
G = nx.DiGraph()

# Add nodes (locations)
G.add_node('Gate A')
G.add_node('Library')
G.add_node('Faculty of Electrical and Electronics')
G.add_node('Cafeteria')
G.add_node('Sports Center')

# Add edges (paths) with weights (distances in meters)
G.add_edge('Gate A', 'Library', weight=100)
G.add_edge('Library', 'Faculty of Electrical and Electronics', weight=150)
G.add_edge('Gate A', 'Cafeteria', weight=200)
G.add_edge('Cafeteria', 'Faculty of Electrical and Electronics', weight=100)
G.add_edge('Gate A', 'Sports Center', weight=250)
G.add_edge('Sports Center', 'Faculty of Electrical and Electronics', weight=150)

# Find the shortest path from Gate A to Faculty of Electrical and Electronics
shortest_path = nx.dijkstra_path(G, source='Gate A', target='Faculty of Electrical and Electronics')

# Define positions for each node for visualization purposes
pos = {
    'Gate A': (0, 0),
    'Library': (1, 2),
    'Faculty of Electrical and Electronics': (3, 2),
    'Cafeteria': (1, -1),
    'Sports Center': (2, -2)
}

# Draw the entire graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')

# Highlight the shortest path
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# Display the plot
plt.title('Shortest Path from Gate A to Faculty of Electrical and Electronics')
plt.show()