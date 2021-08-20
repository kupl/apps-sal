class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph = list(map(set, graph))
        rgraph = defaultdict(set)
        q = deque()
        for (i, nn) in enumerate(graph):
            if not nn:
                q.append(i)
            for j in nn:
                rgraph[j].add(i)
        res = []
        while q:
            j = q.popleft()
            res.append(j)
            for i in rgraph[j]:
                graph[i].remove(j)
                if not graph[i]:
                    q.append(i)
        res.sort()
        return res
