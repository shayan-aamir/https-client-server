import matplotlib
matplotlib.use("TkAgg")
import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define nodes (based on your uploaded diagram)
nodes = [
    "Client", "GET Request", "POST Request", "Server",
    "Login Page", "Register Page", "Response",
    "Register Data", "Login Data", "User Data"
]

G.add_nodes_from(nodes)

# Define edges (connections)
edges = [
    ("Client", "GET Request"),
    ("Client", "POST Request"),

    ("GET Request", "Server"),
    ("POST Request", "Server"),

    ("Server", "Login Page"),
    ("Server", "Register Page"),

    ("Login Page", "Response"),
    ("Register Page", "Response"),

    ("Server", "Register Data"),
    ("Server", "Login Data"),

    ("Register Data", "User Data"),
    ("Login Data", "User Data"),

    ("Server", "Client")  # final response
]

G.add_edges_from(edges)

# Graph layout (custom positions to match your picture)
pos = {
    "Client": (-2, 0),
    "GET Request": (-1, 1),
    "POST Request": (-1, -1),

    "Server": (0, 0),

    "Login Page": (1, 0.7),
    "Register Page": (1, 1.3),

    "Response": (2, 0.7),

    "Register Data": (1, -0.3),
    "Login Data": (1, -1),

    "User Data": (2, -0.6)
}

# Draw the network
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color="#97D9E1", node_size=1800)
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20, width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

plt.title("Client-Server Network Topology for GET and POST Requests", fontsize=14)
plt.axis("off")
plt.show()

