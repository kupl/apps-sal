from collections import defaultdict
from collections import deque

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        n2n = defaultdict(list)
        for x, y, w in edges:
            n2n[x].append([y, w])
            n2n[y].append([x, w])

        minds = [[-1] * n for _ in range(n)]

        for i in range(n):
            minds[i][i] = 0

        for x, y, d in edges:
            minds[x][y] = d
            minds[y][x] = d

        for source in range(n):
            visited = [0] * n
            q = deque()
            q.append(source)
            visited[source] = 1

            while q:
                node = q.popleft()
                for next_node, d in n2n.get(node, []):
                    if not visited[next_node]:
                        q.append(next_node)
                        visited[next_node] = 1
                        if minds[source][next_node] == -1 or minds[source][next_node] > minds[source][node] + d:
                            minds[source][next_node] = minds[source][node] + d
                    else:
                        if minds[source][next_node] == -1 or minds[source][next_node] > minds[source][node] + d:
                            minds[source][next_node] = minds[source][node] + d
                            q.append(next_node)


        min_reach = n
        max_node = 0
        for source in range(n):
            reach_count = 0
            for mind in minds[source]:
                if mind != -1 and  mind <= distanceThreshold:
                    reach_count += 1
            if reach_count <= min_reach:
                max_node = source
                min_reach = reach_count

        return max_node

