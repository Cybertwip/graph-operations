import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def nodes_connected(G, u, v):
        return u in G.neighbors(v)

def hamilton_path(G):
    for i in range(1,G.number_of_nodes() + 1):
        for j in range(1,G.number_of_nodes() + 1):
            for p in nx.all_simple_paths(G, i, j):
                if len(p) == G.number_of_nodes():
                    return p

    return None

def hamilton_circuit(G):
    F = [(G,[list(G.nodes())[0]])]
    n = G.number_of_nodes()
    while F:
        graph,path = F.pop()
        confs = []
        neighbors = (node for node in graph.neighbors(path[-1]) 
                     if node != path[-1]) #exclude self loops
        for neighbor in neighbors:
            conf_p = path[:]
            conf_p.append(neighbor)
            conf_g = nx.Graph(graph)
            conf_g.remove_node(path[-1])
            confs.append((conf_g,conf_p))
        for g,p in confs:
            if len(p)==n:
                if nodes_connected(G, p[0], p[-1]):
                    p.append(p[0])
                return p
            else:
                F.append((g,p))
    return None    

Matrix = []

Coincidences = []

# Graph

# Exercise 3 (A)

'''
Coincidences.append([1, 3])
Coincidences.append([1, 4])
Coincidences.append([1, 5])
Coincidences.append([1, 6])

Coincidences.append([2, 3])
Coincidences.append([2, 4])
Coincidences.append([2, 6])

Coincidences.append([3, 1])
Coincidences.append([3, 2])
Coincidences.append([3, 6])

Coincidences.append([4, 1])
Coincidences.append([4, 2])
Coincidences.append([4, 5])

Coincidences.append([5, 1])
Coincidences.append([5, 3])
Coincidences.append([5, 4])
Coincidences.append([5, 6])

Coincidences.append([6, 1])
Coincidences.append([6, 2])
Coincidences.append([6, 3])
Coincidences.append([6, 5])
'''

# Exercise 3 (B)

Coincidences.append([1, 3])
Coincidences.append([1, 2])
Coincidences.append([1, 5])


Coincidences.append([2, 7])
Coincidences.append([2, 1])


Coincidences.append([3, 1])
Coincidences.append([3, 4])
Coincidences.append([3, 6])
Coincidences.append([3, 8])

Coincidences.append([4, 3])
Coincidences.append([4, 5])
Coincidences.append([4, 8])

Coincidences.append([5, 1])
Coincidences.append([5, 4])
Coincidences.append([5, 8])

Coincidences.append([6, 3])
Coincidences.append([6, 10])

Coincidences.append([7, 2])
Coincidences.append([7, 8])
Coincidences.append([7, 9])

Coincidences.append([8, 3])
Coincidences.append([8, 4])
Coincidences.append([8, 5])
Coincidences.append([8, 7])

Coincidences.append([9, 7])
Coincidences.append([9, 10])

Coincidences.append([10, 9])
Coincidences.append([10, 6])

A = np.array(Coincidences)
G = nx.Graph()

for i in range(len(A)):
    G.add_edge(A[i][0], A[i][1])

print("Vertex degrees")
print(G.degree())

print("Has Hamilton path")
print(str(hamilton_path(G) != None))

print("Has Hamilton circuit")
print(str(hamilton_circuit(G) != None))

if hamilton_path(G) != None:
    hamilton_path = list(hamilton_path(G))

    print("Hamilton path")
    print(hamilton_path)

if hamilton_circuit(G) != None:
    hamilton_circuit = list(hamilton_circuit(G))

    print("Hamilton circuit")
    print(hamilton_circuit)

layout = nx.spring_layout(G)

# Use a list for node_sizes
sizes = []

for i in range(G.number_of_nodes()):
    sizes.append(250)

# Use a list for node colours
color_map = []

for i in range(G.number_of_nodes()):
    color_map.append('b')

# Draw the graph using the layout - with_labels=True if you want node labels.
nx.draw(G, layout, with_labels=True, node_size=sizes)

# Case only vertices and edges
nx.draw_networkx(G, pos=layout)

plt.axis('equal')
plt.show()