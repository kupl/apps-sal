class Solution:
    
    def find(self, c, parents):
        s = c
        while parents[c-1] != -1:
            c = parents[c-1]
        if s != c:
            parents[s-1] = c
        return c
    
    def delete_cycles(self, edges, parents, delete, t):
        for edge in edges:
            c1 = edge[0]
            c2 = edge[1]
            p1 = self.find(c1, parents)
            p2 = self.find(c2, parents)
            # print(f'edge:    {edge}')
            # print(f'p1  p2:  {p1} {p2}')
            # print(f'type:    {t}')
            # print(f'parents: {parents}')
            # print()
            if p1 == p2:
                delete.add((t, c1, c2))
            else:
                parents[p1-1] = p2
        
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        common = [(e[1], e[2]) for e in edges if e[0] == 3]
        type1 = [(e[1], e[2]) for e in edges if e[0] == 1]
        type2 = [(e[1], e[2]) for e in edges if e[0] == 2]
        
        delete = set()
        
        parents1 = [-1] * n
        parents2 = [-1] * n
        
        self.delete_cycles(common, parents1, delete, 3)
        self.delete_cycles(type1, parents1, delete, 1)
        # print(\"-----------------------------------------------\")
        self.delete_cycles(common, parents2, delete, 3)
        self.delete_cycles(type2, parents2, delete, 2)
        
        has_single_parent1 = False
        for p in parents1:
            if p == -1:
                if not has_single_parent1:
                    has_single_parent1 = True
                else:
                    return -1
                
        has_single_parent2 = False
        for p in parents2:
            if p == -1:
                if not has_single_parent2:
                    has_single_parent2 = True
                else:
                    return -1
                
        return len(delete)
                
                
        
        
                

