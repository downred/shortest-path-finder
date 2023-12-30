
class Graph:
    def __init__(self):
        self.adjacency_list = {}


class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, distance, node):
        self.distance = distance
        self.node = node

    def __str__(self):
        return "(" + str(self.distance) + "," + str(self.node.value) + ")"
