import collections
import sys


class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        \"\"\"
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        \"\"\"

        total = sum([r[2] for r in edges])

        if distanceThreshold >= total:
            return n - 1

        MAX_INT = 10001
        dist = [[MAX_INT] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for i, j, d in edges:
            dist[i][j] = dist[j][i] = d

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == MAX_INT or dist[k][j] == MAX_INT:
                        continue

                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        res = 0
        min_cnt = n + 1

        for i, row in enumerate(dist):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt += 1

                if cnt > min_cnt:
                    break

            if cnt <= min_cnt:
                min_cnt = cnt
                res = i

        return res

