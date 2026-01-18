import time
import networkx as nx
import matplotlib.pyplot as plt

# Create topology
G = nx.Graph()

G.add_nodes_from([
    ("Client", {"color": "green"}),
    ("Router1", {"color": "skyblue"}),
    ("Router2", {"color": "skyblue"}),
    ("Server", {"color": "red"}),
])

G.add_edges_from([
    ("Client", "Router1"),
    ("Router1", "Router2"),
    ("Router2", "Server"),
])

# Layout
pos = nx.spring_layout(G, seed=42)

# Compute shortest path
path = nx.shortest_path(G, source="Client", target="Server")
print("Route:", " → ".join(path))

# Draw base network
def draw_network(highlight_edge=None):
    colors = [G.nodes[n]["color"] for n in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1800, font_size=12)
    
    if highlight_edge:
        nx.draw_networkx_edges(
            G, pos, edgelist=[highlight_edge],
            width=3, edge_color="black"
        )

    plt.savefig("packet_step.png")
    plt.clf()

# Animate packet hop-by-hop
for i in range(len(path)-1):
    hop = (path[i], path[i+1])
    print(f"Packet moving: {hop[0]} → {hop[1]}")
    draw_network(hop)
    time.sleep(0.5)

print("Packet reached Server! Output images saved as packet_step.png")

