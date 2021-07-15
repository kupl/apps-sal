class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        
        graph = [set() for _ in range(N)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            
        # count[i]: number of nodes (including i) in the sub-tree started from i (not including visited part)
        count = [1] * N
        ans = [0] * N
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]
                  
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # ans[node] - count[child] = ans[child] + (ans[node] - (ans[child] + count[child]))
                    # ans[child]: result of subtree started from child, x@X
                    # ans[node] - (ans[child] + count[child]): result exclude subtree started from child, y@Y
                    # N - count[child]: number of nodes not in sub-tree started from child, #Y
                    
                    # ans[child] is determined by ans[node] (which has the correct value) and count
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)
        
        # after dfs, only ans[0] has final answer, all other ans[i] is not used anymore
        dfs(0, None)
        
        dfs2(0, None)
        
        return ans
