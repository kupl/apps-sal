class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        from collections import defaultdict
        n = len(s)
        roots = list(range(n))
        sizes = [1]*n
        
        def find(node):
            root = node
            while root != roots[root]:
                root = roots[root]
                
            while node != root:
                next_node = roots[node]
                roots[node] = root
                node = next_node
            
            return root
        
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            
            if root1 == root2:
                return False
            
            if sizes[root2] > sizes[root1]:
                root1, root2 = root2, root1
            
            sizes[root1] += sizes[root2]
            roots[root2] = root1
            
        for x,y in pairs:
            union(x, y)
        
        for i in range(n):
            find(i)
        
        indices = defaultdict(lambda: [])
        chars = defaultdict(lambda: [])
        for i, root in enumerate(roots):
            c = s[i]
            indices[root].append(i)
            chars[root].append(c)
        
        result = [0]*n
        for key in indices.keys():
            for i, v in zip(indices[key], sorted(chars[key])):
                result[i] = v
                
        return \"\".join(result)
        
        
                
