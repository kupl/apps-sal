class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_reverse = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for i in range(len(graph)):
            if not graph[i]:
                indegree[i]
            for nei in graph[i]:
                graph_reverse[nei].append(i)
                indegree[nei]
                indegree[i] += 1
        q = collections.deque([node for node in indegree if indegree[node] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph_reverse[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return sorted(res)
