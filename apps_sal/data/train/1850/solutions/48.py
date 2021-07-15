class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(N)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        \"\"\" 
        O(n^2) TLE.......
        res = [0] * N
        def dfs(idx, cur, parent, cnt):
            for kid in graph[cur]:
                if kid != parent:
                    res[idx] += cnt
                    dfs(idx, kid, cur, cnt+1)
        
        for _ in range(N):
            dfs(_, _, -1, 1)
        return res
        \"\"\"
        
        # print (graph)
        cnt, res = [1] * N, [0] * N
        # res[i] is the distance 
        # cnt[i] is the number of nodes in branch rooted by i (including i itself)
        
        def post(parent, cur): 
            for kid in graph[cur]:
                if kid != parent:
                    post(cur, kid)
                    # add up the numbers of descendent of i's kids
                    cnt[cur] += cnt[kid]         
                    # every descendent of i needs one extra edge to reach i, i.e. the edge (kid,i)
                    res[cur] += res[kid] + cnt[kid] 
                    
        def pre(parent, cur):
            for kid in graph[cur]:     
                if kid != parent:
                    res[kid] = res[cur] - cnt[kid] + N - cnt[kid]
                    pre(cur, kid)
                    
        post(-1, 0)  
        pre(-1, 0)   
        return res
