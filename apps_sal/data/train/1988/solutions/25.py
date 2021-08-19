from collections import deque


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        edges = [{}, {}]
        for i, allEdges in enumerate([red_edges, blue_edges]):
            for edge in allEdges:
                src, tar = edge[0], edge[1]
                edges[i].setdefault(src, []).append(tar)

        def shortedAlterPath(source, target, colour):  # dfs
            queue = deque([source])
            visited = {(colour, source)}
            count = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node == target:
                        return count
                    for nextNode in edges[colour].get(node, []):
                        if (1 - colour, nextNode) in visited:
                            continue
                        visited.add((1 - colour, nextNode))
                        queue.append(nextNode)
                colour = 1 - colour
                count += 1
            return float('inf')
        res = [0] * n
        for dst in range(1, n):
            distance = min(
                shortedAlterPath(0, dst, 0),
                shortedAlterPath(0, dst, 1)
            )
            if distance == float('inf'):
                res[dst] = -1
            else:
                res[dst] = distance
        return res
