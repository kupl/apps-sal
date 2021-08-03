class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        res = []
        degree = [0] * n
        reverseGraph = collections.defaultdict(list)
        q = collections.deque()

        for i in range(n):
            if len(graph[i]) == 0:
                q.append(i)
            for nextNode in graph[i]:
                reverseGraph[nextNode].append(i)
                degree[i] += 1

        while q:
            index = q.popleft()
            res.append(index)
            for nextNode in reverseGraph[index]:
                degree[nextNode] -= 1
                if degree[nextNode] == 0:
                    q.append(nextNode)

        return sorted(res)
