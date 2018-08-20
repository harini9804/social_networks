#Modelling road network of Indian cities

import networkx as nx
import matplotlib.pyplot as plt
import random
import sys

G = nx.Graph()
city_set = ['Delhi','Bangalore','Hyderabad','Chennai','Ahmedabad','Kolkata','Surat','Pune','Jaipur']

for each in city_set:
    G.add_node(each)

#nx.draw(G,with_labels=True)
#plt.show()

def add_random_edge(G,costs):
    c1 = random.choice(list(G.nodes()))
    c2 = random.choice(list(G.nodes()))

    if c1!=c2 and G.has_edge(c1,c2) == 0:
        w = random.choice(costs)
        G.add_edge(c1,c2,weight = w)

costs = []
value = 100

while(value <= 2000):
    costs.append(value)
    value+=100

print(costs)

while(G.number_of_edges()<5):

    c1 = random.choice(list(G.nodes()))
    c2 = random.choice(list(G.nodes()))

    if c1!=c2 and G.has_edge(c1,c2) == 0:
        w = random.choice(costs)
        G.add_edge(c1,c2,weight = w)

#pos = nx.circular_layout(G)
#nx.draw(G,layout = pos, with_labels=True)
#plt.show()

print(nx.is_connected(G))

try:
    l = nx.dijkstra_path_length(G,'Chennai','Bangalore')
except:
    l =10000000
    print('path length = ',l)

x =[0]
y = [l]
for i in range(1,11):
    add_random_edge(G,costs)
    x.append(i)
    try:
        l = nx.dijkstra_path_length(G,'Chennai','Bangalore')
    except:
        l=10000000
    y.append(l)

plt.xlabel('Time')
plt.ylabel('Travelling cost')
plt.title('Change in travelling cost')
plt.plot(x,y)
plt.show()
