import networkx as nx
import matplotlib.pyplot as plt
import random


def display_graph(G,i,ne):
    pos = nx.circular_layout(G)
    if i == '' and ne == '':
        new_node = []
        rest_nodes = G.nodes()
        new_edges = []
        rest_edges = G.edges()
    elif i =='':
        # new_node = [i]
        # rest_nodes =  list(set(G.nodes()) - set(new_node))
        rest_nodes = G.nodes()
        new_edges =  ne
        rest_edges =  list(set(G.edges() ) -  set(new_edges) -  set([(b,a)  for (a,b) in new_edges]))
    nx.draw_networkx_nodes(G,pos,nodelist =  rest_nodes, node_color = 'yellow')
    # nx.draw_networkx_nodes(G,pos,nodelist =  new_node, node_color = 'green')
    nx.draw_networkx_edges(G,pos,edgelist =  new_edges, edge_color = 'green')
    nx.draw_networkx_edges(G,pos,edgelist =  rest_edges, edge_color = 'yellow')
    plt.show()

def erdos_renyi(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r = random.random()
                if r<=p:
                    G.add_edge(i,j)
                    ne = [(i,j)]
                    display_graph(G,'',ne)
                else:
                    ne = []
                    display_graph(G,'',ne)
                    continue

def main():
    n = int(input('Enter val of n'))
    p = float(input('Enter val of p'))

    G = nx.Graph()
    G.add_nodes_from([i for i in range(n)])
    display_graph(G,'','')

    erdos_renyi(G,p)

main()
