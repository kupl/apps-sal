from typing import List
from collections import deque as queue
from functools import lru_cache


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)

        @lru_cache
        def neighbours(i, j):
            return [
                neighbour for neighbour
                in [
                    (i - 1, j) if i > 0 else None,
                    (i + 1, j) if i < n - 1 else None,
                    (i, j - 1) if j > 0 else None,
                    (i, j + 1) if j < n - 1 else None
                ]
                if neighbour is not None
            ]

        # find the first piece of land
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    first = (i, j)
        # mark all pieces on the same land as \"2\",
        # so we can easily diferentiate them from the other island
        q = queue([first])
        # visited also contains all the pieces of land on the second island
        visited = set()
        visited.add(first)
        while q:
            i, j = q.popleft()
            A[i][j] = 2
            for ni, nj in neighbours(i, j):
                if (ni, nj) not in visited and A[ni][nj] == 1:
                    visited.add((ni, nj))
                    q.append((ni, nj))

        min_distance = float('inf')
        for li, lj in visited:
            q = queue([(li, lj, 0)])
            water_visited = set()
            while q:
                i, j, d = q.popleft()
                for ni, nj in neighbours(i, j):
                    if A[ni][nj] == 0 and (ni, nj) not in water_visited and d + 1 < min_distance:
                        water_visited.add((ni, nj))
                        q.append((ni, nj, d + 1))
                    elif A[ni][nj] == 1 and d < min_distance:
                        min_distance = d
                        if min_distance == 1:
                            return 1

        return min_distance
