class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(N)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        size, up, down = [1] * N, [0] * N, [0] * N
        # up[i] is the distance from i's descendant to i
        # down[i] is the distance from others nodes to i
        # size[i] is the number of nodes in branch rooted by i (including i itself)
        
        def post(parent, i): 
            for kid in graph[i]:
                if kid != parent:
                    post(i, kid)
                    # add up the numbers of descendent of i's kids
                    size[i] += size[kid]         
                    # every descendent of i needs one extra edge to reach i, i.e. the edge (kid,i)
                    up[i] += up[kid] + size[kid] 
                    
        def pre(parent, i):
            if parent!=-1:
                # every non-descendent node needs one extra edge to reach i, i.e. the edge (parent,i)
                down[i] = down[parent] + (up[parent] - up[i] - size[i]) + (N-size[i])
                #         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ^^^^^^^^^
                #         from all non-descendent nodes to i's parent      the one extra edge (parent,i)
            for kid in graph[i]:     
                if kid != parent:
                    pre(i, kid)
                    
        post(-1, 0)            
        pre(-1, 0)            
        return [up[i]+down[i] for i in range(N)] 
