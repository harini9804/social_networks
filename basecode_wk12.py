import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def set_path_colours(G,p,p1):
    c = []
    for each in G.nodes():
        if each == p1[0]:
            c.append('red')
        elif each == p1[len(p1) - 1]:
            c.append('red')
        elif each in p and p1:
            c.append('yellow')
        elif each in p:
            c.append('blue')
        elif each in p1:
            c.append('green')
        else:
            c.append('black')
    return c


def add_long_link(G):
    v1 = random.choice(list(G.nodes()))
    v2 = random.choice(list(G.nodes()))
    while(v1==v2):
        v1 = random.choice(list(G.nodes()))
        v2 = random.choice(list(G.nodes()))
    G.add_edge(v1,v2)

def find_best_neighbor(G,c,v):
    dis = G.number_of_nodes()

    for each in G.neighbors(c):
        dis1 = len(nx.shortest_path(H,source = each, target = v))
        if dis1<dis:
            dis = dis1
            choice = each
    return choice
def myopic_search(G,u,v):
    path = [u]
    current = u

    while(1):
        w = find_best_neighbor(G,current,v)
        path.append(w)
        current = w
        if current == v:
            break
    return path

def add_edges(G):
    list_nodes = list(G.nodes())
    # print list_nodes
    n = len(list_nodes)
    for i in range(0,len(list_nodes)):
        # print list_nodes[i], list_nodes[i-1], list_nodes[i-2]

        G.add_edge(list_nodes[i], list_nodes[i-1])
        G.add_edge(list_nodes[i], list_nodes[i-2])
        target = i+1
        if target > n-1:
            target = target - n
        G.add_edge(list_nodes[i], list_nodes[target])
        target = i+2
        if target>n-1:
            target = target - n
        G.add_edge(list_nodes[i], list_nodes[target])


x1 = []
y1 = []
for num in [100,200,300,400,500,600,700,800,900,1000]:

    G = nx.Graph()
    G.add_nodes_from(range(0,num))

    add_edges(G) #add ties based on homophily

    # for each in G.nodes():
    #     print each, ':',
    #     for each1 in G.neighbors(each):
    #         print each1,
    #     print '\n'


    H = G.copy()
    x=[0]
    y=[nx.diameter(G)]
    t=0

    while(t<=G.number_of_nodes()/10):
        add_long_link(G)
        t=t+1
        x.append(t)
        y.append(nx.diameter(G))

    # plt.xlabel('Number of weak ties added')
    # plt.ylabel('Diameter')
    # plt.plot(x,y)
    m = []
    #o = []
    x = []
    t = 0

    for u in range(0,G.number_of_nodes()/2 -1):
        v = u + G.number_of_nodes()/2

        p = myopic_search(G,u,v)
        #p1 = nx.shortest_path(G,source = u,target = v)
        m.append(len(p))
        #o.append(len(p1))
        x.append(t)
        t = t+1

    # plt.plot(x,m,'r')
    # plt.plot(x,o,'b')
    # plt.show()
    # colors = set_path_colours(G,p,p1)
    # nx.draw(G, node_color =colors, with_labels = True)
    # plt.show()

    print np.average(m), G.number_of_nodes()
    x1.append(np.average(m))
    x1.append(G.number_of_nodes())
plt.plot(x1,y1)
plt.show()
