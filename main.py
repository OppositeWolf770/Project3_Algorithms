import networkx as nx
import matplotlib.pyplot as plt
import functions as f


def display_graph(G, edge_labels=None):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=300, font_size=12)

    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.show()

# Logic for Question 1
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

    start_node = 'A'
    end_node = 'J'

    dfs_path = list(nx.dfs_edges(G, source=start_node))
    bfs_path = list(nx.bfs_edges(G, source=start_node))

    def extract_path(edges, end_node):
        path = []
        for u, v in edges:
            path.append(u)
            if v == end_node:
                path.append(v)
                break
        return path

    dfs_path_nodes = extract_path(dfs_path, end_node)

    print(f'DFS Path from {start_node} to {end_node}: {dfs_path_nodes}')

    correct_bfs_path = f.bfs_path(G, start_node, end_node)
    print(f'BFS Path from {start_node} to {end_node}: {correct_bfs_path}')

# Logic for Question 2
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

    # Print the relationship between SCCs and DAG labels
    print("SCC to DAG label mapping:")
    for i, scc in enumerate(sccs):
        print(f"DAG label {i}: {sorted(scc)}")

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


# Logic for Question 3
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

    ### Dijkstra Shortest Path Tree
    source = 'A'
    pred, _ = nx.dijkstra_predecessor_and_distance(G, source)

    # Generate the SPT graph
    T = nx.Graph()
    for node, predecessors in pred.items():
        for pred_node in predecessors:
            T.add_edge(pred_node, node, weight=G[pred_node][node]['weight'])

    # Create the edge labels for the SPT graph
    pos = nx.spring_layout(T)
    edge_labels = {(u, v): d['weight'] for u, v, d in T.edges(data=True)}

    # Draw the SPT graph
    plt.figure(figsize=(6, 4))
    nx.draw(T, pos, with_labels=True, node_color='lightblue', edge_color='grey', node_size=500, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(T, pos, edge_labels=edge_labels, font_size=10)

    # Create the SPT graph title and show it
    plt.title("Shortest Path Tree")
    plt.show()

    ### Minimum Spanning Tree
    T = nx.minimum_spanning_tree(G)

    # Configure the MST Graph for display
    pos = nx.spring_layout(T)
    nx.draw_networkx_nodes(T, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(T, pos, edge_color='grey')
    nx.draw_networkx_labels(T, pos, font_size=12, font_weight='bold', font_family='sans-serif')
    nx.draw_networkx_edge_labels(
        T, pos, edge_labels={(u, v): d["weight"] for u, v, d in T.edges(data=True)}, font_size=10
    )

    # Disable axis, add title, and show MST graph
    plt.axis('off')
    plt.title("Minimum Spanning Tree")
    plt.show()

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