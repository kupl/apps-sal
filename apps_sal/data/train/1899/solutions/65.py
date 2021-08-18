class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        M = len(A)
        N = len(A[0])
        q = collections.deque()
        i0 = None
        j0 = None
        for i in range(M):
            for j in range(N):
                if A[i][j] == 1:
                    i0, j0 = i, j
                    break
            if i0 is not None:
                break

        q.append((i0, j0))
        A[i0][j0] = 2
        vis = set()
        dirs_lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        boarder = set()
        while q:
            i, j = q.popleft()
            for di, dj in dirs_lst:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni > M - 1 or nj < 0 or nj > N - 1:
                    boarder.add((i, j))
                    continue
                if A[ni][nj] == 0:
                    boarder.add((i, j))
                    continue
                if (ni, nj) in vis:
                    continue
                A[ni][nj] = 2
                vis.add((ni, nj))
                q.append((ni, nj))

        vis.clear()
        for i, j in boarder:
            q.append((i, j, 0))
        res = math.inf
        while q:
            i, j, nsteps = q.popleft()
            for di, dj in dirs_lst:
                ni = i + di
                nj = j + dj
                if ni < 0 or ni > M - 1 or nj < 0 or nj > N - 1:
                    continue
                if (ni, nj) in vis:
                    continue
                if A[ni][nj] == 1:
                    res = min(res, nsteps)
                    continue
                vis.add((ni, nj))
                q.append((ni, nj, nsteps + 1))
        return res
