import networkx as nx
import matplotlib.pyplot as plt
import functions as f

def display_graph(G, edge_labels=None):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=12)

    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.show()

def question1():
    graph_dict = {
        "A": {"B", "F", "E"},
        "B": {"C", "F"},
        "C": {"D", "G"},
        "D": {"G"},
        "E": {"F", "I"},
        "F": {"I"},
        "G": {"J"},
        "H": {"K", "L"},
        "I": {"J", "M"},
        "J": {},
        "K": {"O", "L"},
        "L": {"P"},
        "M": {"N"},
        "N": {},
        "O": {},
        "P": {},
    }

    G = nx.Graph(graph_dict)

    display_graph(G)

def question2():
    graph_dict = {
        1: {3},
        2: {1},
        3: {2, 5},
        4: {1, 2, 12},
        5: {6, 8},
        6: {7, 8, 10},
        7: {10},
        8: {9, 10},
        9: {5, 11},
        10: {9, 11},
        11: {12},
        12: set()
    }

    G = nx.DiGraph(graph_dict)

    # display_graph(G)

def question3():
    graph_dict = {
        "A": {"B": {"weight": 22}, "C": {"weight": 9}, "D": {"weight": 12}},
        "B": {"C": {"weight": 35}, "F": {"weight": 36}, "H": {"weight": 34}},
        "C": {"D": {"weight": 4}, "E": {"weight": 65}, "F": {"weight": 42}},
        "D": {"E": {"weight": 33}, "I": {"weight": 30}},
        "E": {"F": {"weight": 18}, "G": {"weight": 23}},
        "F": {"G": {"weight": 39}, "H": {"weight": 24}},
        "G": {"H": {"weight": 25}, "I": {"weight": 21}},
        "H": {"I": {"weight": 19}},
        "I": {},
    }

    G = nx.Graph(graph_dict)

    ############### BFS ###############
    # bfs_result = f.bfs(G, 'A')
    # print("BFS Traversal:", bfs_result)

    # Bellman-Ford algorithm
    d, p = f.bellman_ford(G, "A")

    print("Distances from A:", d)
    print("Predecessors:", p)

    ### Dijkstra's algorithm
    # distances, paths = f.dijkstra(G, 'A')
    #
    # print("Shortest distances from A:", distances)
    #
    # print("Shortest paths:")
    # for node, prev in paths.items():
    #     print(f"{node} <= {prev}")

    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    display_graph(G, edge_labels)

if __name__ == "__main__":
    # question1()
    # question2()
    question3()

