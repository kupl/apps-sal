class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n
    def find(self, i): 
        if self.p[i] != i: 
            self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j): 
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            if self.r[pi] >= self.r[pj]: 
                self.p[pj] = pi
                self.r[pi] += (self.r[pi] == self.r[pj])
            else: 
                self.p[pi] = pj
            return True
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if not edges: return -1
        uf1, n1, uf2, n2 = DSU(n), n, DSU(n), n
        edges.sort(reverse=True, key = lambda x: x[0])
        # t 1:alice, 2:bob, 3:both
        ans = 0
        for t, u, v in edges: 
            print((n1, n2))
            if t == 3: 
                u1, u2 = uf1.find(u-1) == uf1.find(v-1), uf2.find(u-1) == uf2.find(v-1)
                if u1 and u2 : 
                    ans += 1
                else: 
                    if not u1: 
                        uf1.union(u-1, v-1)
                        n1 -= 1
                    if not u2: 
                        uf2.union(u-1, v-1)
                        n2 -= 1
                        
            elif t == 1: 
                if uf1.find(u-1) != uf1.find(v-1): 
                    n1 -= uf1.union(u-1, v-1)
                else:
                    ans += 1
            elif t == 2: 
                if uf2.find(u-1) != uf2.find(v-1): 
                    n2 -= uf2.union(u-1, v-1)
                else:
                    ans += 1
                
                
#             if u1 and uf1.find(u-1) != uf1.find(v-1): 
#                 n1 -= uf1.union(u-1, v-1)
#                 can_delete = False
                    
#             if u2 and uf2.find(u-1) != uf2.find(v-1):
#                 n2 -= uf2.union(u-1, v-1)
#                 can_delete = False
                
            # ans += can_delete
        # print(uf1.p)
        # print(uf2.p)
        print((ans, n1, n2))
        return ans if (n1 <= 1 and n2 <=1) else -1
                
                
            
            
            
            
            

