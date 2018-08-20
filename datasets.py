import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('data_sets/facebook_combined.txt') #takes network and returns graph obj

print(nx.info(G) )
print( nx.number_of_nodes(G))
print( nx.is_directed(G))

G = nx.read_pajek('data_sets/football.net')

print(nx.info(G) )
print( nx.number_of_nodes(G))
print( nx.is_directed(G))


nx.draw(G)
plt.show()