class DisjointSet:
    def __init__(self):
        self.data = {}
        
    def add_node(self, v):
        self.data[v] = v
        
    def find(self, v):
        if (self.data[v] == v):
            return v
        else :
            return self.find(self.data[v])
        
    def union(self, v, w):
        root_v = self.find(v)
        root_w = self.find(w)
        
        self.data[root_v] = root_w
        
    def in_same_set(self, v, w):
        root_v = self.find(v)
        root_w = self.find(w)
        
        return root_v == root_w

def make_spanning_tree(edges, t):
    if (t == 'min'):
        edges = sorted(edges, key=lambda x: x[1])    
    elif (t == 'max'):
        edges = sorted(edges, key=lambda x: -x[1])
        
    
    tree = DisjointSet()
    for edge in edges:
        v, w = edge[0][0], edge[0][1]
        if (v not in tree.data.keys()):
            tree.add_node(v)
        if (w not in tree.data.keys()):
            tree.add_node(w)
    cnt = 0
    output = []
    while (cnt < len(tree.data)-1):
        edge = edges.pop(0)
        v, w = edge[0][0], edge[0][1]
        
        if (not tree.in_same_set(v, w)):
            tree.union(v, w)
            output.append(edge)
            cnt += 1
            
    return output
