class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                edges.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))

        edges.sort(key=lambda x: x[2])

        seen = dict()
        ct = 0
        ans = 0

        for i in range(len(edges)):
            edge = edges[i]

            if edge[0] not in seen or edge[1] not in seen:
                if edge[0] not in seen and edge[1] not in seen:
                    seen[edge[0]] = ct
                    seen[edge[1]] = ct
                    ct += 1
                if edge[0] not in seen and edge[1] in seen:
                    seen[edge[0]] = seen[edge[1]]
                if edge[0] in seen and edge[1] not in seen:
                    seen[edge[1]] = seen[edge[0]]

                ans += edge[2]

            if edge[0] not in seen and edge[1] in seen:
                seen[edge[0]] = seen[edge[1]]

                ans += edge[2]

            if edge[1] not in seen and edge[0] in seen:
                seen[edge[1]] = seen[edge[0]]

                ans += edge[2]

            if edge[0] in seen and edge[1] in seen:
                if seen[edge[0]] != seen[edge[1]]:
                    for key in seen:
                        if key != edge[1] and seen[key] == seen[edge[1]]:
                            seen[key] = seen[edge[0]]

                    seen[edge[1]] = seen[edge[0]]

                    ans += edge[2]

        return ans
