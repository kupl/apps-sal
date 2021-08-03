class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = {}
        for x, y in edges:
            graph[x] = graph.get(x, set())
            graph[x].add(y)
            graph[y] = graph.get(y, set())
            graph[y].add(x)

        queue = [(1, 0, 1)]
        visited = set([1])
        while queue:

            if queue[0][1] == t:
                break
            node, time, p = queue.pop(0)

            neis = [x for x in graph.get(node, []) if x not in visited]
            size = len(neis)
            if neis:
                for nei in neis:
                    queue.append([nei, time + 1, p * 1 / size])
                    visited.add(nei)
            else:
                queue.append((node, time + 1, p * 1))
        while queue:
            node, t, prob = queue.pop(0)
            if node == target:
                return prob
        return 0
