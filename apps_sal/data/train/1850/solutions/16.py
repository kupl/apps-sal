class Node:
    def __init__(self, cur):
        self.cur = cur
        self.edges = set()
        self.num_children = 0
        self.total_dist = 0

    def add_edge(self, Node):
        self.edges.add(Node)
    '''
    @property
    def num_children(self):
        return self.num_children
    
    @num_children.setter
    def num_children(self, num_children):
        self.num_children = num_children
        
    @property
    def total_dist(self):
        return self.total_dist
    
    @total_dist.setter
    def total_dist(self, total):
        self.total_dist = total
        '''

    def __str__(self):
        return str(self.total_dist)


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        print('hello')
        nodes = []
        for i in range(N):
            nodes.append(Node(i))

        for i, j in edges:
            nodes[i].add_edge(nodes[j])
            nodes[j].add_edge(nodes[i])

        self.pre(nodes[0], set())
        self.post(nodes[0], set(), N)

        return [str(i) for i in nodes]

    def pre(self, root, seen):
        seen.add(root)

        root.num_children = 1
        for i in root.edges:
            if i in seen:
                continue
            children, dist = self.pre(i, seen)
            root.num_children += children
            root.total_dist += children + dist

        return root.num_children, root.total_dist

    def post(self, root, seen, N, parent=None):
        seen.add(root)

        if parent != None:
            root.total_dist = parent.total_dist - root.num_children + N - root.num_children

        for i in root.edges:
            if i in seen:
                continue
            self.post(i, seen, N, root)
