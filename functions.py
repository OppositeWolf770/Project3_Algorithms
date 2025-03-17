from collections import deque

import networkx as nx


# Taken from blackboard (Adapted for networkx)
def bfs(graph: nx.Graph, start):
    visited, queue = set(), [start]
    p = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            p.append(vertex)

            # Extend the queue with unvisited neighbors
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return p

# Taken from blackboard (Adapted for networkx)
def bfs_path(graph: nx.Graph, start, goal):
    """
    Finds a shortest path in undirected 'graph' between 'start' and 'goal'.
    If no path is found, returns `None`.
    """
    if start == goal:
        return [start]

    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()

        for neighbor in graph.neighbors(current):
            if neighbor == goal:
                return path + [current, neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current]))

    return None

# Taken from blackboard (Adapted for networkx)
def bfs_paths(graph: nx.Graph, start, goal):
    queue = deque([(start, [])])

    while queue:
        vertex, path = queue.popleft()

        for next in graph.neighbors(vertex):
            if next not in path:
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [vertex]))

# Taken from blackboard (Adapted for networkx)
def dijkstra(graph: nx.Graph, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(graph.nodes())

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None or visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for neighbor, attrs in graph[min_node].items():
            weight = current_weight + attrs.get('weight', 1)
            if neighbor not in visited or weight < visited[neighbor]:
                visited[neighbor] = weight
                path[neighbor] = min_node

    return visited, path

# Taken from blackboard (Adapted for networkx)
# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {}  # Stands for destination
    p = {}  # Stands for predecessor
    for node in graph:
        d[node] = float('Inf')  # We start admitting that the rest of the nodes are very very far
        p[node] = None
    d[source] = 0  # For the source, we know how to reach
    return d, p


def relax(node, neighbor, graph, d, p):
    # If the distance between the node and the neighbor is lower than the one I have now
    if d[neighbor] > d[node] + graph[node][neighbor]['weight']:
        # Record this lower distance
        d[neighbor] = d[node] + graph[node][neighbor]['weight']
        p[neighbor] = node


def bellman_ford(graph, source):
    d, p = initialize(graph, source)

    # Step 2: Relax edges repeatedly (|V| - 1) times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)

    # Step 3: Check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            if d[v] > d[u] + graph[u][v]['weight']:
                raise ValueError("Graph contains a negative-weight cycle")

    return d, p