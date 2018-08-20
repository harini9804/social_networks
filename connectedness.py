import networkx as nx
import random 
import matplotlib.pyplot as plt
import numpy
#Add n number of nodes in the graph
def add_nodes(n):
	G = nx.Graph()
	G.add_nodes_from(range(n))
	return G

#add one random edge

def add_random_edge(G):
	
	v1=random.choice(list(G.nodes()) )
	v2=random.choice(list(G.nodes()) )
	#print v1
	#print v2
	if v1!=v2:
		G.add_edge(v1,v2)
	#	print "added"
	return G

#keep adding random edges in G till it becomes connected

def add_till_connectivity(G):
	while(nx.is_connected(G) == False):
		G = add_random_edge(G)

	return G

#creates an instance of the entire process and returns the number of edges 
def create_instance(n):
	G = add_nodes(n)
	G = add_till_connectivity(G)
	return G.number_of_edges()

#Average it over 4 instances

def create_avg_instance(n):
	list1 =[]
	for i in range(0,100):
		list1.append(create_instance(n))
	return numpy.average(list1)

#Plot the desired for different number of edges
def plot_connectivity():
	x = []
	y = []
	i=10 #i is the number of edges

	while( i<=200):
		print i
		x.append(i)
		y.append(create_avg_instance(i))
		i=i+10

	
	plt.xlabel('number of nodes')
	plt.ylabel('number of edges reqd to connect graph')
	plt.title('Emergence of connectivity')
	plt.plot(x,y)

	x1=[]
	y1=[]
	i=10
	while( i<=200 ):
		print i
		x1.append(i)
		y1.append(i*float(numpy.log(i)/2))
		i+=10

	plt.plot(x1,y1)
	plt.show()