class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph:
            return []
        n = len(graph)
        adj = collections.defaultdict(set)
        for i in range(n):
            for j in graph[i]:
                adj[j].add(i)
        res = [i for i in range(n) if not graph[i]]
        outdegree = [len(graph[i]) for i in range(n)]
        Q = collections.deque(res)
        while Q:
            cur = Q.popleft()
            for i in adj[cur]:
                outdegree[i] -= 1
                if outdegree[i] == 0:
                    res.append(i)
                    Q.append(i)
        return sorted(res)
