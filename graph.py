"""
Python program for graph deployment and adjacency matrix
"""

# Class to represent adjacency list of the node


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# A class to represent a graph
# Size of the array will be number of vertices


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]*self.V

    def add_edge(self, src, dest):
        # adding node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    # adding the source node to the destination as
    # it is undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # method to print the graph
    def print_graph(self):
        for i in range(self.V):
            print('Adjacency list of vertex {}\n head'.format(i), end='')
            temp = self.graph[i]
            while temp:
                print(' -> {}'.format(temp.vertex), end='')
                temp = temp.next
            print('\n')


# driver code
if __name__ == '__main__':
    vertices = 5
    graph = Graph(vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
