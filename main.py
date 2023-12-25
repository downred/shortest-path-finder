from dijkstra import dijkstra
from graph import Graph, Node, Edge

g = Graph()

node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

g.adjacency_list = {
    node_a: [Edge(3, node_b), Edge(6, node_c), Edge(4, node_d)],
    node_b: [Edge(3, node_a), Edge(2, node_c), Edge(3, node_e)],
    node_c: [Edge(6, node_a), Edge(2, node_b), Edge(3, node_e),  Edge(3, node_f)],
    node_d: [Edge(4, node_a), Edge(6, node_f)],
    node_e: [Edge(3, node_b), Edge(3, node_c), Edge(1, node_f)],
    node_f: [Edge(6, node_d), Edge(1, node_e)],
}

print(g.adjacency_list)

# Test Dijkstra's algorithm
start_node = node_a
dijkstra(g, start_node)
