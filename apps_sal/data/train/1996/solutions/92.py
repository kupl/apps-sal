from collections import deque


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        graph = list(map(set, graph))
        rgraph = [set() for _ in range(N)]
        safe = [False] * N
        q = deque()
        for (fr, tos) in enumerate(graph):
            if not tos:
                q.append(fr)
            for to in tos:
                rgraph[to].add(fr)
        while q:
            to = q.popleft()
            safe[to] = True
            for fr in rgraph[to]:
                graph[fr].remove(to)
                if not graph[fr]:
                    q.append(fr)
        return [i for (i, v) in enumerate(safe) if v]
