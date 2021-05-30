import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

Matrix = []

Coincidences = []

# Graph

# Exercise 1
'''
Coincidences.append(['A', 'B', 20])
Coincidences.append(['A', 'C', 15])
Coincidences.append(['A', 'D', 4])

Coincidences.append(['B', 'A', 40])
Coincidences.append(['B', 'C', 19])
Coincidences.append(['B', 'D', 5])

Coincidences.append(['C', 'A', 7])
Coincidences.append(['C', 'D', 2])

Coincidences.append(['D', 'A', 5])
Coincidences.append(['D', 'B', 6])
Coincidences.append(['D', 'C', 6])
'''

# Directed Graph
'''
Coincidences.append(['A', 'B', 20])
Coincidences.append(['A', 'C', 15])

Coincidences.append(['B', 'A', 40])
Coincidences.append(['B', 'C', 19])

Coincidences.append(['C', 'A', 7])
Coincidences.append(['C', 'B', 2])
'''

# Exercise 2
'''
Coincidences.append(['A', 'B', 5])

Coincidences.append(['B', 'C', 3])

Coincidences.append(['C', 'D', 1])

Coincidences.append(['C', 'A', 2])

Coincidences.append(['D', 'C', 1])

Coincidences.append(['D', 'B', 4])
'''

# Exercise 4
'''
Coincidences.append(['Jorge', 'Luis', 1])
Coincidences.append(['Jorge', 'Maite', 1])

Coincidences.append(['Luis', 'Jorge', 1])
Coincidences.append(['Luis', 'Ana', 1])

Coincidences.append(['Ana', 'Luis', 1])

Coincidences.append(['Maite', 'Jorge', 1])
'''

# Exercise 6

Coincidences.append(['Julio', 'Google', 30])
Coincidences.append(['Julio', 'Bing', 19])
Coincidences.append(['Julio', 'Ecosia', 8])

Coincidences.append(['Pedro', 'Google', 10])
Coincidences.append(['Pedro', 'Yahoo', 49])
Coincidences.append(['Pedro', 'Ecosia', 14])

Coincidences.append(['Ramon', 'Yahoo', 17])
Coincidences.append(['Ramon', 'Bing', 20])
Coincidences.append(['Ramon', 'Ecosia', 33])

Coincidences.append(['Alberto', 'Google', 25])
Coincidences.append(['Alberto', 'Bing', 16])

A = np.array(Coincidences)

G = nx.Graph()
#G = nx.DiGraph()

for i in range(len(A)):
    G.add_edge(A[i][0], A[i][1], weight=A[i][2])


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


# Get weights of each edge and assign to labels
labels = nx.get_edge_attributes(G, "weight")

# Draw edge labels using layout and list of labels

# Case only vertices and edges
#nx.draw_networkx(G, pos=layout)

# Case weights
nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)

plt.axis('equal')

plt.show()