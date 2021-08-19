class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = [False] * len(graph)
        rev = [set() for _ in range(len(graph))]
        queue = collections.deque()
        for (i, nodes) in enumerate(graph):
            if not nodes:
                queue.append(i)
            else:
                for node in nodes:
                    rev[node].add(i)
        while queue:
            curr = queue.popleft()
            safe[curr] = True
            for j in rev[curr]:
                graph[j].remove(curr)
                if len(graph[j]) == 0:
                    queue.append(j)
        return [i for (i, val) in enumerate(safe) if val]
