import networkx as nx
import random
import matplotlib.pyplot as plt


def set_all_B(G):
    for each in G.nodes():
        G.node[each]['action'] = 'B'

def set_A(G, list1):
    for each in list1:
        G.node[each]['action'] = 'A'

def get_colors(G):
    list1=[]
    for each in G.nodes():
        if G.node[each]['action'] == 'B':
            list1.append('red')
        else:
            list1.append('blue')
    return list1

def find_neigh(each, c, G):
    num =0;
    for each1 in G.neighbors(each):
        if G.node[each1]['action'] == c:
            num = num+1
    return num

def recalculate_options(G):
    dict1 = {}
    # Payoff(A) = a = 4
    # Payoff(A) = b = 3
    a = 3
    b = 2
    for each in G.nodes():
        num_A = find_neigh(each,'A',G)
        num_B = find_neigh(each,'B',G)
        payoff_A = a*num_A
        payoff_B = b*num_B
        if payoff_A >=payoff_B:
            dict1[each] = 'A'
        else:
            dict1[each]='B'

    return dict1

def reset_node_attributes(G, action_dict):
    for each in action_dict:
        G.node[each]['action'] = action_dict[each]

def terminate_1(c,G):
    f = 1
    for each in G.nodes():
        if G.node[each]['action']!=c:
            f=0
            break
    return f

def terminate(G,count):
    flag1 = terminate_1('A',G)
    flag2 = terminate_1('B',G)
    if flag1 == 1 or flag2 == 1 or count >=100:
        return 1
    else:
        return 0

G = nx.Graph()

G.add_edges_from([(0,1),(0,6),(1,2),(1,8),(1,12),(2,9),(2,12),(3,4),(3,9),(3,12),(4,5),(4,12),(5,6),(5,10),(6,8),(7,8),(7,9),(7,10),(7,11),(8,9),(8,10),(8,11),(9,10),(9,11),(10,11)])

list2=[[0,1,2,3],[0,2,3,4],[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,12],[2,3,4,12],[0,1,2,3,4,5],[0,1,2,3,4,5,6,12]]

for list1 in list2:

    set_all_B(G)

    list1 = [4,1]
    set_A(G,list1)

    colors = get_colors(G)
    nx.draw(G,node_color=colors, node_size=800)
    plt.show()

    #reweigh options based on neighbours

    flag=0
    count=0
    while(1):
        flag = terminate(G,count)
        if flag ==1:
            break
        count = count +1

        action_dict = recalculate_options(G)

        reset_node_attributes(G,action_dict)
        colors = get_colors(G)

    c = terminate_1('A',G)
    if c == 1:
        print 'cascade complete'
    else:
        print 'cascade incomplete'
    nx.draw(G,node_color=colors, node_size=800)
    plt.show()
