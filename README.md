# 🚀 Dijkstra_GUI

## Assignment Requirements 📜

1. **Core Task**:
   - Complete the implementation of the Dijkstra algorithm in `controllers.py`.
   - Use the provided GUI program to visualize the algorithm.
   - Implement missing code sections marked with `# TODO` in the file.

2. **Submission Files**:
   - Python source code files (`controllers.py` and others) that can execute the program.
   - Add clear comments to explain how each part of the implemented code works.
   - Include a report (~2 pages) detailing how the algorithm was implemented and showing execution results (e.g., screenshots).

3. **Additional Task**:
   - Research the **Poisoned Reverse** technique to address the `count-to-infinity` problem in Distance Vector algorithms.
   - Document findings in the report.

4. **Rules**:
   - Strictly no copying of code. Any detected plagiarism will result in zero marks for all involved parties.

---

## Project Overview 🌟
This project implements the **Dijkstra Algorithm** to calculate the shortest path between nodes in a graph and visualizes the results in a **GUI interface**. The goal is to enhance understanding of data structures and algorithms by integrating them with a practical graphical interface.

### Background 🧠
The Dijkstra algorithm is widely used in network optimization, pathfinding in maps, and solving graph-based problems. This project allows users to create and manipulate graphs while exploring shortest path computations visually.

### Key Features ✨
1. **Dijkstra Algorithm Implementation**:
   - Calculates the shortest path from a starting node to other nodes within a given graph.
   - Evaluates paths based on weights assigned to edges.

2. **GUI Interface**:
   - Enables the creation of graph nodes and edges.
   - Visualizes shortest path results based on user input.
   - Intuitive interface for better understanding of pathfinding.

3. **Additional Task**:
   - Investigates the `count-to-infinity` issue in Distance Vector algorithms and explores the **Poisoned Reverse** technique as a solution.

---

## File Structure 📂

- `controllers.py`: Core logic for the Dijkstra algorithm.
- `main.py`: Manages GUI events and the overall application flow.
- `models.py`: Defines data models for graphs, nodes, and edges.
- `views.py`: Implements GUI rendering and user interactions.

---

## Setup and Execution ⚙️

### Requirements
- Python 3.8 or higher
- Required packages: `pygame`, `tkinter`

### Installation
```bash
# Install required packages
pip install pygame
```

### Running the Program
```bash
python main.py
```

---

## Implementation Details 🔍

### Dijkstra Algorithm (`controllers.py`)
1. **`init`**:
   - Initializes the graph, setting all node distances to infinity and the start node's distance to 0.

2. **`search_min`**:
   - Finds and returns the node with the minimum distance in the queue.
   - Iterates through the queue, comparing `graph.distances[node]` to identify the minimum.

3. **`update_distances`**:
   - Updates the shortest distances for nodes connected to the current node.
   - Modifies `graph.distances` and sets predecessor nodes in `graph.preds`.

4. **`dijkstra`**:
   - Combines the above functions to execute the Dijkstra algorithm step by step.
   - Uses a queue to process nodes and excludes completed nodes from further exploration.

5. **`find_path`**:
   - Builds the shortest path from the start node to the target node using calculated data.

### GUI Interface (`main.py`, `views.py`)
1. **Node and Edge Creation**:
   - Allows users to dynamically construct graph structures.
2. **Path Visualization**:
   - Highlights the computed shortest path in red on the GUI.
3. **Intuitive Interaction**:
   - Supports node movement, deletion, and connection using a mouse.

---

## Major Code Updates ✍️

### `controllers.py` Detailed Changes

#### **`search_min` Function**:
   - Implemented logic to find the node with the minimum distance from the queue.
   - Compares `graph.distances[node]` values to determine the minimum.

   ```python
   for node in queue:
       if graph.distances[node] < mini:
           mini = graph.distances[node]
           node_m = node
   return node_m
   ```

#### **`update_distances` Function**:
   - Calculates weights to update shortest paths for adjacent nodes.
   - Updates `graph.distances` and sets the predecessor for each updated node.

   ```python
   if graph.distances[node_x] > graph.distances[node] + weight_x:
       graph.distances[node_x] = graph.distances[node] + weight_x
       graph.preds[node_x] = node
   ```

#### **`dijkstra` Function**:
   - Integrates `search_min` and `update_distances` to perform the algorithm iteratively.
   - Removes nodes from the queue after processing to streamline operations.

   ```python
   while len(queue) != 0:
       min_n = search_min(graph, queue)
       update_distances(graph, min_n)
       queue.remove(min_n)
   ```

#### **`find_path` Function**:
   - Uses the results of the Dijkstra algorithm to construct the shortest path from the start node to the destination node.

---

## Results and Demonstration 🎨

1. **Graph Creation and Shortest Path Calculation**:
   - Users can add nodes and edges via the GUI, then select start and end nodes to compute the shortest path.
   - The resulting path is visually emphasized in red.

2. **Execution Example**:
   - Below is an example showing nodes, edges, and the computed shortest path:

---

## Additional Task: Poisoned Reverse 🛠️

### Problem Definition
The `count-to-infinity` problem in Distance Vector algorithms arises from routing loops, where incorrect path costs propagate infinitely.

### Solution: Poisoned Reverse
1. Nodes transmit "infinite" path costs for specific routes to prevent loops.
2. This ensures that incorrect routing information does not propagate back to its source.

#### Key Principle
- If Node A updates its route to Node C via Node B, it sets the cost of Node C to infinity when informing Node B, breaking the loop.

More detailed explanations are provided in the accompanying report.
