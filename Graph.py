class Graph:
    def __init__ (self):
        self.nodes = {}
        
    def add_node(self, node):
        self.nodes[node] = []
        
    def add_edge(self, source, destination):
        self.nodes[source].append(destination)
        
my_graph = Graph()
my_graph.add_node('A')
my_graph.add_node('B')
my_graph.add_node('C')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'A')