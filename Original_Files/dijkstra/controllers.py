"""
Controllers module

This is where we find the dijkstra methods
"""

import math
from models import Connection, Node, Graph


def init(graph: Graph, start_node: Node):
    """
    This function initialized the graph distances for later calculations
    """
    for node in graph.nodes:
        graph.distances[node] = math.inf
    graph.distances[start_node] = 0


def search_min(graph: Graph, queue: list) -> Node:
    """
    This function search and returns the node that has the minimal distance
    """
    mini = math.inf
    node_m = None
    # TODO: Iterate through queue to find node_m that has the minimum distance and return it.
    for node in queue:



    return node_m


def find_min_distance(graph: Graph, node1: Node, node2: Node) -> int:
    """
    This function returns the minimum distance from node1 to node2
    """
    dijkstra(graph, node1)
    return graph.distances[node2]


def get_weight(graph: Graph, node1: Node, node2: Node) -> int:
    """
    This function returns the weight between two nodes
        :param G: graph
        :param node1: start node
        :param node2: destination node
        :type G: Graph
        :type node1: Node
        :type node2: Node
        :return: the weight between node1 and node2
        :rtype: int
    """
    weight = -1
    for connection in graph.connections:
        if (connection.nodes[0] == node1 and connection.nodes[1] == node2) or \
                (connection.nodes[0] == node2 and connection.nodes[1] == node1):
            weight = connection.weight
    return weight


def update_distances(graph: Graph, node: Node):
    """
    This function updates the distance of the adjacent nodes from a given node
        :param G: the graph
        :param node: the targeted node
        :type G: Graph
        :type node: Node
    """
    for node_x, _ in node.neighbors:
        weight_x = get_weight(graph, node, node_x)
        if graph.distances[node_x] > graph.distances[node] + weight_x:
            # TODO: update the shortest distance to node_x.

            # TODO: Update the predecessor to node_x as the current node.



def dijkstra(graph: Graph, start_node: Node):
    """
    This method runs the dijkstra algorithm with the start node as the given node \
        and updates the distances array accordingly
    """
    init(graph, start_node)
    queue = graph.nodes.copy()

    while len(queue) != 0:
        # TODO: Find the node with minimum distance (Hint: Use the search_min function above)

        # TODO: Update the distance to its neighbors (Hint: Use the update_distances function above)

        # TODO: Remove the min. distance node from the queue



def find_path(graph: Graph, start_node: Node, dest_node: Node, ret_list=[]) -> list[Connection]:
    """
    This method find the best route (minimal distance path) between start_node and dest_node.
    This method should ONLY be run after the dijkstra algorithm is applied!
    """
    if start_node == dest_node:
        return None

    pred_node = graph.preds[dest_node]
    conn = None
    for conn in graph.connections:
        if pred_node in conn.nodes and dest_node in conn.nodes:
            break
    if conn is None:
        raise Exception(f'Connection between {pred_node} and {dest_node} not found!')

    ret_list.append(conn)
    find_path(graph, start_node, pred_node, ret_list)

    return ret_list
