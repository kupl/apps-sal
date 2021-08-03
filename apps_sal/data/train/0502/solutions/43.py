from collections import deque


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        if graph is None or len(graph) == 0 or len(graph[0]) == 0 or len(initial) == 0:
            return None

        n = len(graph)
        m = len(graph[0])
        k = len(initial)
        initial.sort()

        result = sys.maxsize
        idx = None
        for i in range(k):
            temp_q = initial[:]
            temp_q.pop(i)
            temp_q = deque(temp_q)
            temp_visited = set(temp_q)

            self.helper(graph, temp_q, temp_visited)
            if result > len(temp_visited):
                result = len(temp_visited)
                idx = initial[i]

        return idx

    def helper(self, graph, temp_q, temp_visited):

        n, m = len(graph), len(graph[0])

        while temp_q:
            curr = temp_q.popleft()
            for col in range(m):
                if col in temp_visited or graph[curr][col] == 0:
                    continue
                temp_visited.add(col)
                temp_q.append(col)
