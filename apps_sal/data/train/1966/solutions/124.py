class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        (m, n) = (len(mat), len(mat[0]))

        def v1d(h):
            ans = 0
            length = 0
            for v in h:
                length = length + 1 if v else 0
                ans += length
            return ans
        for i in range(m):
            h = [1] * n
            for idown in range(i, m):
                for j in range(n):
                    h[j] &= mat[idown][j]
                res += v1d(h)
        return res

    def numSubmat_dp_style(self, mat: List[List[int]]) -> int:
        allones = set()
        (m, n) = (len(mat), len(mat[0]))
        q = collections.deque()
        for (i, j) in itertools.product(range(m), range(n)):
            if mat[i][j]:
                q.append((i, j, 1, 1))
                allones.add((i, j, 1, 1))
        while q:
            (i, j, r, c) = q.popleft()
            if i + r < m and (i + r, j, 1, c) in allones:
                q.append((i, j, r + 1, c))
                allones.add((i, j, r + 1, c))
            if j + c < n and (i, j + c, r, 1) in allones:
                q.append((i, j, r, c + 1))
                allones.add((i, j, r, c + 1))
        return len(allones)
