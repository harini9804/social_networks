import networkx as nx
import matplotlib.pyplot as plt
import random

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

seed = [3,8]
list1 = ic(G,seed)
