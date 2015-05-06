import networkx as nx 
import matplotlib.pyplot as plt

def drawGraph(graph):
	pos=nx.random_layout(graph)
	redList = []
	blackList = []
	for x in xrange(graph.number_of_nodes()):
		if graph.node[x]["color"] == "r":
			redList.append(x)
		else:
			blackList.append(x)
	nx.draw_networkx_nodes(graph,pos,
                       nodelist=redList,
                       node_color='r',
                       node_size=500,
                   alpha=0.8)
	nx.draw_networkx_nodes(graph,pos,
                       nodelist=blackList,
                       node_color='b',
                       node_size=500,
                   alpha=0.8)
	nx.draw_networkx_edges(graph,pos,width=1.0,alpha=0.5)
	plt.show()

def ok(graph):
	for x in graph.edges(data=True):
		if x[0]!=x[1]:
			if graph.node[x[0]]['connect']!=[]:
				graph.node[x[0]]['connect'].append(graph.node[x[1]]['color'])
				graph.node[x[1]]['connect'].append(graph.node[x[0]]['color'])
			elif graph.node[x[0]]['connect'].

	return True

def modMST(graph):
	result = nx.graph()
	sort = sorted(g.edges(data=True), key = lambda t: t[2].get('weight'),reverse=True)
	

fin = open("1.in", "r")
N = int(fin.readline())
d = [[] for i in xrange(N)]
for i in range(N):
    d[i] = [int(x) for x in fin.readline().split()]
c = fin.readline()

g = nx.Graph()
for x in xrange(N):
	if c[x] == 'R':
		col = "r"
	else:
		col = "b" 
	g.add_node(x, color = col,connect=[])
for x in xrange(N):
	for y in xrange(x,N):
		g.add_edge(x,y,weight=d[x][y])


