import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

Matrix = []

Coincidences = []

# Graph

# Exercise 2 (A)

'''
Coincidences.append(['1', '6'])
Coincidences.append(['1', '7'])
Coincidences.append(['1', '2'])

Coincidences.append(['2', '1'])
Coincidences.append(['2', '3'])
Coincidences.append(['2', '4'])
Coincidences.append(['2', '7'])

Coincidences.append(['3', '2'])
Coincidences.append(['3', '4'])

Coincidences.append(['4', '3'])
Coincidences.append(['4', '2'])
Coincidences.append(['4', '7'])
Coincidences.append(['4', '5'])

Coincidences.append(['5', '4'])
Coincidences.append(['5', '7'])
Coincidences.append(['5', '6'])

Coincidences.append(['6', '1'])
Coincidences.append(['6', '5'])
'''

# Exercise 2 (B)

Coincidences.append(['1', '2'])
Coincidences.append(['1', '4'])

Coincidences.append(['2', '1'])
Coincidences.append(['2', '3'])
Coincidences.append(['2', '4'])
Coincidences.append(['2', '5'])

Coincidences.append(['3', '2'])
Coincidences.append(['3', '4'])

Coincidences.append(['4', '3'])
Coincidences.append(['4', '2'])
Coincidences.append(['4', '1'])
Coincidences.append(['4', '5'])

Coincidences.append(['5', '4'])
Coincidences.append(['5', '2'])

A = np.array(Coincidences)
G = nx.Graph()

for i in range(len(A)):
    G.add_edge(A[i][0], A[i][1])

print("Vertex degrees")
print(G.degree())

print("Has Eulerian path")
print(nx.has_eulerian_path(G))

print("Is Eulerian")
print(nx.is_eulerian(G))

if nx.has_eulerian_path(G):
    eulerian_path = list(nx.eulerian_path(G))

    print("Eulerian path")
    print(eulerian_path)

if nx.is_eulerian(G):
    eulerian_circuit = list(nx.eulerian_circuit(G))

    print("Eulerian circuit")
    print(eulerian_circuit)



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