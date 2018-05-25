import numpy as np
import pylab as plt
import networkx as nx
import random
# import import pdb

room_list = [(1,3),(3,1),(1,5),(5,1),(0,4),(4,0),(2,3),(3,2),(3,4),(4,3),(4,5),(5,4),(5,5)]
goal = 5
gamma = 0.9
#goal = random.randint(0,5)
# print(goal)
NUM_ROOMS = 6
G = nx.DiGraph()
G.add_edges_from(room_list)
pos = nx.spring_layout(G)
nx.draw_networkx_edges(G,pos,arrows=True)
nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_labels(G,pos)
# show figure of graph
# plt.show(block = False)
# construct reward table
R =  -1*np.ones((NUM_ROOMS,NUM_ROOMS), dtype=int)
for i_zer in range(0, len(room_list)):
    R[room_list[i_zer]] = 0
# convert room_list from array to list
room_list = map(list, room_list)
room_list = list(room_list)
room_list = np.reshape(room_list,(len(room_list),2))
# index of destination goal
ind_goal = np.array(np.where(room_list[:,1] == goal))
# convert index to array
R_goal_index = np.array(room_list[ind_goal])
# assign reward value of 100 in R
for i_tup in range(0,len(ind_goal[0,:])):
    R_goal_index2 = tuple(R_goal_index[0,i_tup,:])
    # print(R_goal_index2)
    R[R_goal_index2] = 100

# Q matrix init
Q = np.zeros((NUM_ROOMS,NUM_ROOMS))
# print('Q matrix is {}'.format(Q))
# current state coordinates
current_state = 3
# next available states
# pdb.set_trace()
next_step_av = R[:,current_state]
print('Next available states are {}'.format(next_step_av))
print(next_step_av[4])
# vector with all next possible states
nex_st = np.where(next_step_av >= 0)[0]
print('Next states are {}'.format(nex_st))
# next state
next_state = max(next_step_av[nex_st])
print('Next state is {}'.format(next_state))
action = random.choice(nex_st)
print('Action is {}'.format(action))
Q[current_state,action] = R[current_state,action]+gamma*next_state
# print('Q matrix is {}'.format(Q))