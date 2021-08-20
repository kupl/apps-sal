class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        re = [set() for _ in range(N)]
        q = collections.deque([])
        for (i, v) in enumerate(graph):
            if not v:
                q.append(i)
            for j in v:
                re[j].add(i)
        res = []
        while q:
            temp = q.popleft()
            res.append(temp)
            for renei in re[temp]:
                graph[renei].remove(temp)
                if len(graph[renei]) == 0:
                    q.append(renei)
        return sorted(res)
