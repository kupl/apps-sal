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
                #下面不需要ans.append(i),因为在color从1到2的时候就已经被加进了ans！！
                # ans.append(i)
                return True
            elif color[i] == 0:
                color[i] = 1
                for j in graph[i]:
                    #不能直接dfs(j),因为这样dfs(j)有可能是false，但是却没有退出，导致后面还会执行
                    # color[i] = 2 ans.append(i) return True
                    # dfs(j)
                    #下面是要对false判断，如果是false直接退出
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
            
        

