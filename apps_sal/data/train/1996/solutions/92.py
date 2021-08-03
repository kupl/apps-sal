from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)

        graph = list(map(set, graph))  # fr -> tos
        rgraph = [set() for _ in range(N)]  # to -> frs
        safe = [False] * N

        # this will contain safe nodes (that are not pointed to)
        q = deque()

        for fr, tos in enumerate(graph):
            if not tos:
                # safe
                q.append(fr)
            for to in tos:
                rgraph[to].add(fr)

        while q:
            to = q.popleft()
            safe[to] = True
            for fr in rgraph[to]:
                graph[fr].remove(to)
                if not graph[fr]:
                    # safe after removal of a to that is safe
                    q.append(fr)

        return [i for i, v in enumerate(safe) if v]
