class Solution:
    
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        edge_type = {1:True, 2:False, 3:True}
        self.father = [i for i in range(n)]
        self.count = n
        self.travel(n, edges, edge_type)
        count_a = self.count
        
        edge_type = {1:False, 2:True, 3:True}
        self.father = [i for i in range(n)]
        self.count = n
        self.travel(n, edges, edge_type)
        count_b = self.count
        
        if count_a > 1 or count_b > 1:
            return -1
        
        edge_type = {1:False, 2:False, 3:True}
        self.father = [i for i in range(n)]
        self.count = n
        self.travel(n, edges, edge_type)
        count_both = self.count
        
        delete_both = len([i for i in edges if i[0] in [3]]) - (n - count_both)
        delete_a = len([i for i in edges if i[0] in [1, 3]]) - (n - 1) 
        delete_b = len([i for i in edges if i[0] in [2, 3]]) - (n - 1) 
        
        return delete_a + delete_b - delete_both
        
        
    
    def travel(self, n, edges, edge_type):
        
        for edge in edges:
            if edge_type[edge[0]]:
                self.union(edge[1] - 1, edge[2] - 1)

             
        
    def find(self, idx):
        if self.father[idx] == idx:
            return idx
        else:
            self.father[idx] = self.find(self.father[idx])
            return self.father[idx]
                    
                    
    def union(self, idx1, idx2):
        father_a = self.find(idx1)
        father_b = self.find(idx2)
        if father_a != father_b:
            self.count -= 1
            self.father[father_a] = father_b

