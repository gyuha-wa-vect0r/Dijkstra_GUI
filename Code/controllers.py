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
    This function search and returns the noㄴde that has the minimal distance
    """
    mini = math.inf
    node_m = None
    # TODO: Iterate through queue to find node_m that has the minimum distance and return it.
    # TODO 해석: 큐를 순회해서 가장 짧은 거리를 가진 노드(node_m)를 찾아 리턴하세요.
    # 이는 다익스트라 알고리즘에서 현재 상태에서 다음으로 탐색해야 할 노드를 선택
    #   -> 그래프의 모든 노드 중에서 아직 방문하지 않은 노드 중에서 최단 거리 값을 가진 노드를 찾아 리턴
    # 이 함수는 다익스트라 알고리즘의 매번 순회 할 때마다 다음으로 탐색할 노드를 선택하기 위해 호출됨
    for node in queue:                   # 큐에 있는 노드들로 순회함
        if graph.distances[node] < mini: # 만약 현재 순회하는 노드의 거리가 누적 최솟값보다 작다면? 
            mini = graph.distances[node] # 현재 노드 거리로 최솟값 갱신
            node_m = node                # 최소 거리를 가지는 노드로 갱신
        
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
            # 기존의 거리가 (graph.distances[node_x]) 새 경로를 통해 계산된 거리보다 길다면, 
            # 새 경로를 더 짧은 거리로 판단하여 업데이트함.

            # 현재 노드에서 인접 노드로 이동할 때의 가중치를 고려하여, 
            # 새로운 경로를 통해 이동하는 것이 더 짧다면 
            # 해당 노드까지의 최단 거리를 갱신해야 함.

            # TODO: update the shortest distance to node_x.
            # TODO 해석: node_x까지의 최단 거리를 갱신하세요.
            # 현재 노드까지의 거리로부터 (graph.distances[node]) 
            # 인접 노드로의 가중치를 (weight_x) 더해 새 경로의 거리를 계산.
            graph.distances[node_x] = graph.distances[node] + weight_x 
            
            # TODO: Update the predecessor to node_x as the current node.
            # TODO 해석: node_x의 이전 노드를 현재 노드로 갱신하세요.
            # graph.preds[node_x]는 노드 node_x의 predecessor(이전) 노드를 기록해둠.
            # 현재 노드 node를 node_x의 이전 노드로 설정
            graph.preds[node_x] = node



def dijkstra(graph: Graph, start_node: Node):
    init(graph, start_node)
    queue = graph.nodes.copy() 
    # 원본 그래프로 굴리면 변경이 누적되기에, 복사 떠서 사용
    # queue = graph.nodes로 할당할 경우, 
    # queue와 graph.nodes는 같은 리스트를 참조하게 되므로 하나를 변경하면 
    # 다른 하나도 똑같이 변경됨!!!

    while len(queue) != 0:
        # TODO: Find the node with minimum distance. (Hint: Use the search_min function above)
        # TODO 해석: 최소 거리를 가진 노드를 찾으세요. (힌트: 위에서 구현한 search_min 함수를 사용하세요~)
        # 위에서 선언된 search_min에 graph, queue를 파라미터로 넣어서 실행
        # graph: 알고리즘이 작동할 전체 그래프 정보를 포함, 거리와 경로를 저장하고 관리함
        # queue: 아직 처리되지 않은 노드의 목록으로 매 단계에서 최소 거리를 가진 노드를 선택하고 관리함
        # search_min 함수를 호출하여 현재 남아 있는 큐에서 최소 거리를 가진 노드를 찾아 min_n에 저장
        min_n = search_min(graph, queue)

        # TODO: Update the distance to its neighbors (Hint: Use the update_distances function above)
        # TODO 해석: 선택된 노드와 연결된 인접 노드들의 거리를 업데이트하시오 (힌트: 위에서 구현한 update_distances 함수를 사용하세요~)
        # 현재 선택된 노드(min_n)에서 시작해서 이 노드와 연결된 모든 인접 노드의 거리를 확인하고 갱신함
        update_distances(graph, min_n)

        # TODO: Remove the min. distance node from the queue
        # TODO 해석: 최소 거리 노드를 큐에서 제거하세요.
        # min_n은 이미 최단거리로 찍혔기 때문에 탐색을 마무리하기 위하여,
        # 이 노드를 큐에서 제거하고 이후 단계에서 처리되지 않도록 함
        queue.remove(min_n)



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
