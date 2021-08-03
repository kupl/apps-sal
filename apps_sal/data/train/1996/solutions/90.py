from collections import defaultdict, deque


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        q = deque()
        ans = [False] * n

        graph_map = dict()
        r_graph_map = defaultdict(set)
        for i in range(n):
            graph_map[i] = set(graph[i])

            if not graph[i]:
                q.append(i)
            for out in graph[i]:
                r_graph_map[out].add(i)

        while q:
            safe_i = q.popleft()
            ans[safe_i] = True
            for in_id in r_graph_map[safe_i]:
                graph_map[in_id].remove(safe_i)
                if len(graph_map[in_id]) == 0:
                    q.append(in_id)
        return [i for i, safe in enumerate(ans) if safe]
