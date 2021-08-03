class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]

        # vert_slid_win = [0]*(K*2+1)
        # for ii in range(0, K+1):
        #     if ii>=0 and ii<m:
        #         vert_slid_win[ii] = sum([mat[ii][c] for c in range(0, K+1) if c >=0 and c<m])

        for i in range(m):

            hori_slid_win = [0] * (K * 2 + 1)
            for jj in range(0, K + 1):
                if jj >= 0 and jj < n:
                    hori_slid_win[jj + K] = sum([mat[r][jj] for r in range(i - K, i + K + 1) if r >= 0 and r < m])

            for j in range(n):
                res[i][j] = sum(hori_slid_win)
                hori_slid_win.pop(0)
                if j + K + 1 < n:
                    hori_slid_win.append(sum([mat[r][j + K + 1] for r in range(i - K, i + K + 1) if r >= 0 and r < m]))
                # print(hori_slid_win)
        return res
