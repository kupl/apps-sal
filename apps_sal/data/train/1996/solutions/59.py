class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False for _ in range(n)]

        rgraph = [set([]) for _ in range(n)]

        queue = collections.deque([])

        for i in range(n):
            if not graph[i]:
                queue.append(i)
            else:
                for j in graph[i]:
                    rgraph[j].add(i)

        while queue:
            curr_node = queue.popleft()

            safe[curr_node] = True

            for prev in rgraph[curr_node]:
                graph[prev].remove(curr_node)

                if len(graph[prev]) == 0:
                    queue.append(prev)
        return [i for i, s in enumerate(safe) if s]
