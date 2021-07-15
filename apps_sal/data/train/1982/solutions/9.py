class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 0:
            return False
        
        dlikelist = [[] for i in range(N)]
        for p in dislikes:
            dlikelist[p[0]-1].append(p[1]-1)
            dlikelist[p[1]-1].append(p[0]-1) #Dislike is mutual
            
        seen = [-1] * N
        group = [-1] * N
        parent = [-1] * N
        
        def dfs(src):
            seen[src] = 1
            if parent[src] == -1:
                group[src] = 0
            else:
                group[src] = 1 -group[parent[src]]
            
            for p in dlikelist[src]:
                if seen[p] == -1:
                    parent[p] = src
                    if dfs(p) == False:
                        return   False
                else:
                    if group[p] == group[src]:
                        return False
            return True
            

        for i in range(N):
            if seen[i] == -1:
                if dfs(i) == False:
                    return False
        return True
        
        
        

