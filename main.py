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

    dfs = nx.dfs_tree(G, 'A')
    bfs = nx.bfs_tree(G, 'A')

    print(f'DFS Nodes: {dfs.nodes}')
    print(f'BFS Nodes: {bfs.nodes}')

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

    # Find strongly connected components
    sccs = list(nx.strongly_connected_components(G))
    print("Strongly Connected Components:", sccs)

    # Build the meta graph (condensed graph)
    meta_graph = nx.condensation(G)

    # Topologically sort the meta graph
    topological_order = list(nx.topological_sort(meta_graph))
    print("Topological Order of the Meta Graph:", topological_order)

    # Relabel meta graph nodes with SCC contents
    scc_labels = {i: ','.join(map(str, sorted(scc))) for i, scc in enumerate(sccs)}
    meta_graph = nx.relabel_nodes(meta_graph, scc_labels)

    # Draw the original graph
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=700, font_weight='bold')
    plt.title("Original Graph")

    # Draw the condensed meta graph with SCC labels
    plt.subplot(1, 2, 2)
    nx.draw(meta_graph, with_labels=True, node_color='lightgreen', node_size=700, font_weight='bold')
    plt.title("Meta Graph (SCCs)")

    plt.show()



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

    dijkstra_path = nx.single_source_dijkstra_path(G, 'A')
    print("Dijkstra's path from A:", dijkstra_path)

    # edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    # display_graph(G, edge_labels)

if __name__ == "__main__":
    while True:
        choice = input("Select question to view (Q to quit):")

        if choice == '1':
            question1()
        elif choice == '2':
            question2()
        elif choice == '3':
            question3()
        else:
            quit()
