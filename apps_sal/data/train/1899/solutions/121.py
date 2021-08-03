from random import randint
from collections import deque, Counter, defaultdict
from heapq import heappush, heappop, heapify
from scipy.special import comb, perm
from bisect import bisect, bisect_left, bisect_right


class Solution:
    def shortestBridge(self, A):
        que, row, col, visited = deque(), len(A), len(A[0]), set()

        def dfs(i, j):
            if i < 0 or i > row - 1 or j < 0 or j > col - 1 or (i, j) in visited:
                return
            visited.add((i, j))
            if A[i][j] == 0:
                que.append((i, j))
                return
            for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                dfs(ni, nj)

        found = False
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break

        cnt = 0
        while que:
            n = len(que)
            for _ in range(n):
                i, j = que.popleft()
                if A[i][j] == 1:
                    return cnt
                for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if 0 <= ni < row and 0 <= nj < col and (ni, nj) not in visited:
                        que.append((ni, nj))
                        visited.add((ni, nj))
            cnt += 1
