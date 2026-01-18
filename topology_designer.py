import networkx as nx
import matplotlib.pyplot as plt

def draw_topology(topology="star", n=6):
    G = nx.Graph()

    if topology == "star":
        G.add_node("Center")
        for i in range(n):
            G.add_edge("Center", f"N{i}")

    elif topology == "mesh":
        for i in range(n):
            for j in range(i+1, n):
                G.add_edge(f"N{i}", f"N{j}")

    elif topology == "ring":
        for i in range(n):
            G.add_edge(f"N{i}", f"N{(i+1)%n}")

    elif topology == "custom":
        G.add_edges_from([
            ("Client1", "Router1"),
            ("Client2", "Router1"),
            ("Router1", "Server1"),
            ("Router1", "Server2"),
        ])

    pos = nx.spring_layout(G, seed=10)
    nx.draw(G, pos, with_labels=True, node_size=1800, node_color="lightblue")
    plt.savefig(f"{topology}_topology.png")
    plt.clf()
    print(f"{topology} topology saved as {topology}_topology.png")

# Examples:
draw_topology("star")
draw_topology("mesh")
draw_topology("ring")
draw_topology("custom")

