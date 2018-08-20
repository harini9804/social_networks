import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('data_sets/facebook_combined.txt') #takes network and returns graph obj

print nx.info(G)