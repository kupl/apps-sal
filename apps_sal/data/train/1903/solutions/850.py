from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        n = len(points)

        edges = [[3000000, 0] for i in range((n * (n - 1)) // 2)]
        idx = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges[idx] = [abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j]
                idx += 1
        edges.sort()

        ret = 0

        i = 0
        k = 0
        child = defaultdict(lambda: [])
        while i < n - 1:
            noCycle = True
            visited = {}
            stack = [[edges[k][1], -1], [edges[k][2], -1]]
            while len(stack) > 0:
                node = stack.pop()
                if node[0] in visited:
                    noCycle = False
                    break
                else:
                    for ch in child[node[0]]:
                        if ch != node[1]:
                            stack.append([ch, node[0]])
                    visited[node[0]] = True
            if noCycle:
                i += 1
                ret += edges[k][0]
                child[edges[k][1]].append(edges[k][2])
                child[edges[k][2]].append(edges[k][1])
            k += 1
        return ret
