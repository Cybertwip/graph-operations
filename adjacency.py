import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from itertools import permutations

def are_isomorphic(G, H):
    """Check whether two graphs G and H are isomorphic.
    
    Note: This function is brute force and very slow.
    
    args:
        G: a networkx Graph
        H: a networkx Graph
    
    returns:
        True if G and H are isomorphic.
        False if G and H are not isomorphic.
    """
    n = len(G.nodes())
    m = len(H.nodes())
    if n != m:
        return False
    if sorted(list(G.degree())) != sorted(list(H.degree())):
        return False
    else:
        a_g = nx.adjacency_matrix(G)
        vertex_perms = list(permutations(H.nodes(), m))
        for i in vertex_perms:
            a_h = nx.adjacency_matrix(H, i)
            if (a_h.todense() == a_g.todense()).all():
                #print(list(zip(G.nodes(), i)), "is an isomorphism") 
                return True
        return False

Matrix = []

CoincidencesA = []
CoincidencesB = []

# Graph

# Exercise 5 (A)


CoincidencesA.append([1, 3])
CoincidencesA.append([1, 4])
CoincidencesA.append([1, 5])
CoincidencesA.append([1, 6])

CoincidencesA.append([2, 3])
CoincidencesA.append([2, 4])
CoincidencesA.append([2, 6])

CoincidencesA.append([3, 1])
CoincidencesA.append([3, 2])
CoincidencesA.append([3, 6])

CoincidencesA.append([4, 1])
CoincidencesA.append([4, 2])
CoincidencesA.append([4, 5])

CoincidencesA.append([5, 1])
CoincidencesA.append([5, 3])
CoincidencesA.append([5, 4])
CoincidencesA.append([5, 6])

CoincidencesA.append([6, 1])
CoincidencesA.append([6, 2])
CoincidencesA.append([6, 3])
CoincidencesA.append([6, 5])


# Exercise 5 (B)

CoincidencesB.append([1, 2])
CoincidencesB.append([1, 4])
CoincidencesB.append([1, 6])

CoincidencesB.append([2, 1])
CoincidencesB.append([2, 3])
CoincidencesB.append([2, 5])
CoincidencesB.append([2, 6])

CoincidencesB.append([3, 2])
CoincidencesB.append([3, 4])
CoincidencesB.append([3, 6])

CoincidencesB.append([4, 1])
CoincidencesB.append([4, 3])
CoincidencesB.append([4, 5])

CoincidencesB.append([5, 1])
CoincidencesB.append([5, 2])
CoincidencesB.append([5, 4])
CoincidencesB.append([5, 6])

CoincidencesB.append([6, 1])
CoincidencesB.append([6, 2])
CoincidencesB.append([6, 3])
CoincidencesB.append([6, 5])

A = np.array(CoincidencesA)
B = np.array(CoincidencesB)
G1 = nx.Graph()
G2 = nx.Graph()

for i in range(len(A)):
    G1.add_edge(A[i][0], A[i][1])

for i in range(len(B)):
    G2.add_edge(B[i][0], B[i][1])

a_g1 = nx.to_numpy_matrix(G1)
a_g2 = nx.to_numpy_matrix(G2)

a_g1 = np.squeeze(np.asarray(a_g1))
a_g2 = np.squeeze(np.asarray(a_g2))


matrix1 = ""
for row in a_g1:
    for value in row:
        matrix1 = matrix1 + str(int(value))
    matrix1 = matrix1 + "\n"

matrix2 = ""
for row in a_g2:
    for value in row:
        matrix2 = matrix2 + str(int(value))
    matrix2 = matrix2 + "\n"

print("Matrix 1")
print(matrix1)

print("Matrix 2")
print(matrix2)

print("Adjacency for Wolfram")


print("Matrix 1")

row_counter = 1
column_counter = 1
matrix1 = ""
for row in a_g1:
    for value in row:
        int_value = int(value)
        if(int_value == 1):
            matrix1 = matrix1 + str(row_counter) + "->" + str(column_counter) + ", "
        
        column_counter = column_counter + 1
    row_counter = row_counter + 1
    column_counter = 1


matrix1 = list(matrix1)
matrix1[-1] = ""
matrix1[-2] = ""

matrix1 = "".join(matrix1)
print(matrix1)

print("\n")
print("Matrix 2")

row_counter = 1
column_counter = 1
matrix1 = ""
for row in a_g2:
    for value in row:
        int_value = int(value)
        if(int_value == 1):
            matrix1 = matrix1 + str(row_counter) + "->" + str(column_counter) + ", "
        
        column_counter = column_counter + 1
    row_counter = row_counter + 1
    column_counter = 1


matrix1 = list(matrix1)
matrix1[-1] = ""
matrix1[-2] = ""

matrix1 = "".join(matrix1)
print(matrix1)