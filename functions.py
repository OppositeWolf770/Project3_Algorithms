from collections import deque

import networkx as nx

# Taken from blackboard (Adapted for networkx)
def dfs_path(graph: nx.Graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        vertex, path = stack.pop()

        if vertex not in visited:
            if vertex == goal:
                return path

            visited.add(vertex)

            for neighbor in graph.neighbors(vertex):
                stack.append((neighbor, path + [neighbor]))

    return None

# Taken from blackboard (Adapted for networkx)
def dfs_paths(graph: nx.Graph, start, goal):
    stack = [(start, [start])]

    while stack:
        vertex, path = stack.pop()

        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))


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