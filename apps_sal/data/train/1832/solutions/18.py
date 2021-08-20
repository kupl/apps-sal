class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = collections.defaultdict(dict)
        for edge in edges:
            g[edge[0]][edge[1]] = edge[2] + 1
            g[edge[1]][edge[0]] = edge[2] + 1
        hq = [(-M, 0)] * len(g[0])
        if len(hq) == 0:
            return 1
        visited = {}
        while hq:
            (rem_move, node) = heapq.heappop(hq)
            if node in visited:
                continue
            visited[node] = rem_move
            for nei in list(g[node].keys()):
                weight = g[node][nei]
                if nei not in visited and rem_move + weight <= 0:
                    heapq.heappush(hq, (rem_move + weight, nei))
        res = len(visited)
        counted = set()
        for edge in edges:
            edge_tuple = (min(edge[:2]), max(edge[:2]))
            if edge[0] in visited and edge[1] in visited and (edge_tuple not in counted):
                counted.add(edge_tuple)
                res += min(g[edge[0]][edge[1]] - 1, -(visited[edge[0]] + visited[edge[1]]))
            elif edge[0] in visited:
                res = res + -visited[edge[0]]
            elif edge[1] in visited:
                res = res + -visited[edge[1]]
        return res
