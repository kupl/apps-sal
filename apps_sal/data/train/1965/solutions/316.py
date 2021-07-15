import collections
class Solution:
    def find(self, i): 
        if self.root[i]==i: return self.root[i]
        self.root[i]=self.find(self.root[i])
        return self.root[i]
    
    def union(self, i, j):
        ri=self.find(i)
        rj=self.find(j)
        self.root[rj]=ri
        return 
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
            dA=collections.defaultdict(list)
            dB=collections.defaultdict(list)
            d=collections.defaultdict(list)
            A=0
            B=0
            res=0
            for t,u,v in edges:
                if t==1: 
                    dA[u-1].append(v-1)
                elif t==2: 
                    dB[u-1].append(v-1)
                else: d[u-1].append(v-1)
            self.root=[i for i in range(n)]
            
            for u in d:
                for v in d[u]:
                    if self.find(u)==self.find(v): res+=1
                    else: self.union(u,v)
            
            
            temp=self.root.copy()
            for u in dA:
                for v in dA[u]:
                    if self.find(u)==self.find(v):
                        res+=1
                    else:
                        self.union(u,v)
            if len(set([self.find(i) for i in range(n)]))>1: return -1
            self.root=temp
            
            for u in dB:
                for v in dB[u]:
                    if self.find(u)==self.find(v):
                        res+=1
                    else:
                        self.union(u,v)
            if len(set([self.find(i) for i in range(n)]))>1: return -1
            return res
            

