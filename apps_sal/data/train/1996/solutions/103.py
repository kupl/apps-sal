class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # table = collections.defaultdict(list)
        # for i in range(len(graph)):
        #     table[i] = graph[i]
        
        #寻找从一个点出发，是否有环
        def dfs(i):
            if color[i] == 1:
                return False
            elif color[i] == 2:
                # ans.append(i)
                return True
            elif color[i] == 0:
                color[i] = 1
                if graph[i]:
                    for j in graph[i]:
                        # dfs(j)
                        if not dfs(j):
                            return False
                color[i] = 2
                ans.append(i)
                return True
                
                
        ans = []
        color = [0] * len(graph)
        for i in range(len(graph)):
            if color[i] == 0:
                dfs(i)
        return sorted(ans)
            
        

