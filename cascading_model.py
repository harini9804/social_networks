import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def ic(G,seed):
    print seed
    just_inf = list(seed)
    infected = list(seed)
    while(1):
        print just_inf, infected
        if len(just_inf) == 0:
            return infected
        tmp = []
        for each in just_inf:
            for each1 in G.neighbors(each):
                r = random.uniform(0,1)
                if r<0.5 and each1 not in infected and each1 not in tmp:
                    tmp.append(each1)
        for each in tmp:
            infected.append(each)
        just_inf = list(tmp)




G = nx.Graph()
G.add_edges_from([(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),
(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])


dict_deg = {}
dict_cl = {}
dict_bw = {}
dict_cr = {}


for each in G.nodes():
    dict_deg[each] = G.degree(each)
    dict_cl[each] = nx.closeness_centrality(G,each)
    dict_bw[each] = nx.betweenness_centrality(G,each)
    dict_cr[each] = nx.core_number(G)[each]

dict_cascade = {}

for each in G.nodes():
    c= []
    for num in range(0,1000):
        seed = [each]
        i = ic(G,seed)
        c.append(len(i))
    dict_cascade[each] = np.average(c)

sorted_dict_cascade = sorted(dict_cascade, key = dict_cascade.get, reverse = True)
sorted_dict_cl = sorted(dict_cascade, key = dict_cl.get, reverse = True)
sorted_dict_deg = sorted(dict_cascade, key = dict_deg.get, reverse = True)
sorted_dict_cr = sorted(dict_cascade, key = dict_cr.get, reverse = True)
sorted_dict_bw = sorted(dict_cascade, key = dict_bw.get, reverse = True)

print ' Nodes sorted acc to deg'
print sorted_dict_deg
print ' Nodes sorted acc to closeness'
print sorted_dict_cl
print ' Nodes sorted acc to betweenness'
print sorted_dict_bw
print ' Nodes sorted acc to coreness'
print sorted_dict_cr
print ' Nodes sorted acc to cascade model'
print sorted_dict_cascade
