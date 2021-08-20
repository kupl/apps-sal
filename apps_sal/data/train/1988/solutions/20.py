class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        res = [float('inf') for i in range(n)]
        for edge in red_edges:
            graph[edge[0]].add((edge[1], 'r'))
        for edge in blue_edges:
            graph[edge[0]].add((edge[1], 'b'))
        qu = [(0, 0, None)]
        visited = set()
        while qu:
            (node, dist, prev) = qu.pop(0)
            res[node] = min(res[node], dist)
            for nbr in graph[node]:
                if prev == None or (prev != nbr[1] and (node, nbr[0], nbr[1]) not in visited):
                    qu.append((nbr[0], dist + 1, nbr[1]))
                    visited.add((node, nbr[0], nbr[1]))
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] = -1
        return res
