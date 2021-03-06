import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0, 4, 3, 0],
              [0, 0, 0, 1],
              [0, 3, 0, 1],
              [2, 0, 0, 0]])
G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

print(nx.dijkstra_path(G, 0, 3))

nx.draw(G)
plt.show()