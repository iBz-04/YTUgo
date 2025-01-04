# Shortest Route Visualization for Yıldız Technical University


<p align="center">
  <img src="https://res.cloudinary.com/diekemzs9/image/upload/v1736030244/Screenshot_2025-01-04_222119_h10axo.png" alt="Image 1" width="615">
</p>


## Project Overview

This Python project calculates and visualizes the shortest walking route between the main entrance (Gate A) and the Faculty of Electrical and Electronics at Yıldız Technical University using first using manually using Djiskra's Algorithm + NetworkX and then for more accuracy I use OpenRouteService and Folium.

## Algorithm

**Dijkstra algorithm**: is a popular algorithm for finding the shortest paths in a graph. The algorithm works by iteratively selecting the node with the smallest known distance from the start node, expanding its neighbors, and updating the shortest distance for those neighbors. This process continues until the shortest path to the target node is found.

### Key Steps in the Algorithm:

1. **Graph Representation**: The campus is represented as a graph where nodes represent locations (e.g., Gate A, Library, Cafeteria, Faculty) and edges represent paths with weights (distances in meters).
2. **Shortest Path**: The algorithm calculates the shortest path between the specified source (Gate A) and target (Faculty of Electrical and Electronics) nodes using the graph structure.
3. **Path Visualization**: Once the shortest path is found, it is highlighted in the graph visualization using Matplotlib and NetworkX.

## Working Principle

- Computes the shortest walking path between two specified locations.
- Visualizes the route on an interactive map.
- Highlights key waypoints along the path.

## Dependencies

- `matplotlib`: Library for visualization.
- `networkX`: Library for maniuplating complex networks.
- `openrouteservice`: Python client for OpenRouteService API.
- `folium`: Python library for creating interactive maps.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/iBz-04/YTUgo.git
   ```
