import networkx as nx
import matplotlib.pyplot as plt
import random
N= 10
G = nx.complete_graph(10)
for (u,v) in G.edges():
    G[u][v]['sign'] = random.choice([-1,1])

labels = dict( ( (u,v), G[u][v]['sign'] ) for (u,v) in G.edges() )

nx.draw(G,with_labels=False)
nx.draw_networkx_labels(G,pos=nx.circular_layout(G),labels = dict( (n,n) for n in G.nodes() ))
nx.draw_networkx_edge_labels(G,pos = nx.circular_layout(G),edge_labels = labels)
plt.show()
