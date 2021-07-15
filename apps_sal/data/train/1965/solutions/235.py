from collections import defaultdict

class Solution:
    
    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent [i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
  
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else : 
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def helpMST(self, adj_list, n):
        
        parent = []
        rank = [0] * (n+1)
        result = []
        
        for node in range(n+1): 
            parent.append(node)
        
        for t, u, v in adj_list:
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:     
                result.append((t,u,v)) 
                self.union(parent, rank, x, y)
                
        parent_count = 0
        for index, num in enumerate(parent[1:]):
            if index + 1 == num:
                parent_count += 1
        
        return parent_count == 1, result
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        adj_list1 = []
        adj_list2 = []
        
        common = set()
        for t, u, v in edges:
            if t == 3:
                common.add((u, v))
                adj_list1.append((t,u,v))
                adj_list2.append((t,u,v))
        
        for t, u, v in edges:
            if t in (1,2) and (u,v) not in common:
                if t == 1:
                    adj_list1.append((t,u,v))
                elif t == 2:
                    adj_list2.append((t,u,v))
                    
        result = set()
        
        if len(adj_list1) < n-1 or len(adj_list2) < n-1:
            return -1
        elif len(adj_list1) == n-1 and len(adj_list2) == n - 1:
            result = result.union(set(adj_list2))
            result = result.union(set(adj_list1))
            return len(edges) - len(result)
        
        if len(adj_list1) > n-1:
            possible, res = self.helpMST(adj_list1, n)
            if not possible:
                return -1
            result = result.union(set(res))
        else:
            result = result.union(set(adj_list1))
        
        if len(adj_list2) > n-1:
            possible, res = self.helpMST(adj_list2, n)
            if not possible:
                return -1
            result = result.union(set(res))
        else:
            result = result.union(set(adj_list2))
            
        return len(edges) - len(result)

