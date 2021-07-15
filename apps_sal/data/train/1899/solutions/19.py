class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if not len(A) or not len(A[0]):
            return 0
        m, n = len(A), len(A[0])

        def neighbors(i, j):
            for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= ni < m and 0 <= nj < n:
                    yield ni, nj

        def dfs(i, j, seen, island):
            if (i, j) not in seen:
                seen.add((i, j))
                for ni, nj in neighbors(i, j):
                    if A[ni][nj] == 1:
                        dfs(ni, nj, seen, island)
                    else:
                        island.add((i, j))

        def find_island():
            seen = set()
            island = set()
            for i in range(m):
                for j in range(n):
                    if A[i][j] == 1:
                        dfs(i, j, seen, island)
                        return seen, island
        
        seen, island = find_island()
        q = collections.deque(list([(x, 0) for x in island]))
        
        while q:
            (i, j), cnt = q.popleft()
            for ni, nj in neighbors(i, j):
                if (ni, nj) not in seen:
                    seen.add((ni, nj))
                    if A[ni][nj] == 1:
                        return cnt
                    q.append(((ni, nj), cnt + 1))
        
        return -1

