from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def explore(i):  # checks for cycle (true)
            colors[i] = 1
            for j in graph[i]:
                if ((colors[j] == 0 and explore(j)) or colors[j] == 1):
                    return True
            colors[i] = 2
            res.append(i)
            return False
        colors = [0 for i in range(len(graph))]
        #0 - white, 1 - gray, 2 - black
        # 0 - unvisited, 1 - under processing, 2 - visited
        res = []
        for i in range(len(graph)):
            if colors[i] == 0:
                explore(i)
        return sorted(res)
