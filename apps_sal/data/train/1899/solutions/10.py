class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        r = len(A)
        c = len(A[0])
        path = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        idx = []        
        for i in range(r):
            for j in range(c):
                if A[i][j] == 1:
                    idx.append((i, j))
        queue = collections.deque([idx[0]])
        seen = {tuple(idx[0])}
        island = collections.deque([(idx[0][0], idx[0][1], 0)])
        while queue:
            x, y = queue.popleft()
            for i in path:
                a = x + i[0]
                b = y + i[1]
                if 0 <= a < r and 0 <= b < c and A[a][b] == 1 and (a, b) not in seen:
                    queue.append((a, b))
                    seen.add((a, b))
                    island.append((a, b, 0))
        while island:
            x, y, z = island.popleft()
            for i in path:
                a = x + i[0]
                b = y + i[1]
                if 0 <= a < r and 0 <= b < c and (a, b) not in seen:
                    if A[a][b] == 0:
                        island.append((a, b, z + 1))
                        seen.add((a, b))
                    else:
                        return z
