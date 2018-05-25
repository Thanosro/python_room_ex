import numpy as np
import pylab as plt
import networkx as nx
import random

room_list = [(1,3),(3,1),(1,5),(5,1),(0,4),(4,0),(2,3),(3,2),(3,4),(4,3),(4,5),(5,4),(5,5)]
goal = 5
NUM_ROOMS = 6
G = nx.DiGraph()
G.add_edges_from(room_list)
pos = nx.spring_layout(G)
nx.draw_networkx_edges(G,pos,arrows=True)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_labels(G,pos)
plt.show()

R =  -1*np.ones((NUM_ROOMS,NUM_ROOMS), dtype=int)
for i_zer in len(room_list):
    R[room_list[i_zer]] = 0
