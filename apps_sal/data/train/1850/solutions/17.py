class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        
        memo=collections.defaultdict(set)
        
        for i,j in edges:
            memo[i].add(j)
            memo[j].add(i)
            
        
        res=[0]*N
        nodes=[1]*N
        
        def t(root,pre):
            for i in memo[root]:
                if i!=pre:
                    t(i,root)
                    nodes[root]+=nodes[i]
                    res[root]+=res[i]+nodes[i]
        
        def t1(root,pre):
            for i in memo[root]:
                if i!=pre:                    
                    res[i]=res[root]-2*nodes[i]+N
                    t1(i,root)
                    
                    
        t(0,-1)
        t1(0,-1)
        
        return res
