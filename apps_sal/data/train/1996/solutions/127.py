from collections import deque, defaultdict


class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        safe_states = [False] * N
        another_graph = defaultdict(set)
        q = collections.deque()
        for (i, js) in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                another_graph[j].add(i)
        print((graph, another_graph))
        while q:
            u = q.popleft()
            safe_states[u] = True
            for v in another_graph[u]:
                graph[v].remove(u)
                if len(graph[v]) == 0:
                    q.append(v)
        return [u for (u, v) in enumerate(safe_states) if v]
