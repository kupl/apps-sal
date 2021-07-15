from collections import defaultdict

class DisjointSet:
    class Node:
        def __init__(self, x):
            self.val = x
            self.parent = self
            self.rank = 0
            
    def __init__(self, node_num):
        self.val_to_node = {}
        
        for val in range(node_num):
            self.val_to_node[val] = DisjointSet.Node(val)
            
    def find(self, x):
        return self._find(self.val_to_node[x]).val
    
    def _find(self, node):
        if node.parent is node:
            return node
        
        node.parent = self._find(node.parent)
        return node.parent
    
    def union(self, val1, val2):
        root1 = self._find(self.val_to_node[val1])
        root2 = self._find(self.val_to_node[val2])
        
        if root1 is root2:
            return
        
        if root2.rank > root1.rank:
            root1, root2 = root2, root1
            
        if root1.rank == root2.rank:
            root1.rank += 1
        
        root2.parent = root1
            

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s
        
        disjoint_set = DisjointSet(len(s))
        
        for u, v in pairs:
            disjoint_set.union(u, v)
        
        connected_components = defaultdict(list)
        
        for i in range(len(s)):
            connected_components[disjoint_set.find(i)].append(i)
        
        res = [None] * len(s)
        for group in list(connected_components.values()):
            sorted_chars = sorted([s[i] for i in group])
            
            for idx, s_i in enumerate(sorted(group)):
                res[s_i] = sorted_chars[idx]
                
        return ''.join(res)

