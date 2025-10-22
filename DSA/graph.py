"""

Graph implementation uing Hash Table/Dict data structure (Adjacent) 

"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        if vertex in self.adj_list:
            return False
        self.adj_list[vertex] = set()
        return True
    
    def add_edge(self,vertex1, vertex2):
        if vertex1 not in self.adj_list:
            self.adj_list[vertex1] = set() 
        if vertex2 not in self.adj_list: 
            self.adj_list[vertex2] = set()
        
        self.adj_list[vertex1].add(vertex2)
        self.adj_list[vertex2].add(vertex1)
        return True
    
    def remove_edge(self,vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list[vertex1]:
            self.adj_list[vertex1].remove(vertex2)
        
        if vertex2 in self.adj_list and vertex1 in self.adj_list[vertex2]:
            self.adj_list[vertex2].remove(vertex1)
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)
            del self.adj_list[vertex]
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,':',self.adj_list[vertex])                 # type: ignore`

g1 = Graph() 
g1.add_vertex('A')
g1.add_vertex('B')
g1.add_vertex('C')
g1.add_vertex('D')
g1.add_edge('A','B')
g1.add_edge('B','C')
g1.add_edge('C','D')
g1.add_edge('D','A')
g1.add_edge('A','C')
g1.print_graph()   
g1.remove_edge('A','B')
g1.print_graph() 
g1.remove_vertex('A')
g1.print_graph()                      
