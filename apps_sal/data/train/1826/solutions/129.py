class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat
        R, C = len(mat), len(mat[0])
        l2r = [[0] * C for _ in range(R)]
        t2b = [[0] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                l2r[r][c] += mat[r][c]
                if c != 0:
                    l2r[r][c] += l2r[r][c - 1]

                t2b[r][c] += mat[r][c]
                if r != 0:
                    t2b[r][c] += t2b[r - 1][c]

        ret = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                temp = 0
                left = max(0, c - K)
                right = min(C - 1, c + K)
                for _r in range(max(0, r - K), min(R, r + K + 1)):
                    if left == 0:
                        temp += l2r[_r][right]
                    else:
                        temp += l2r[_r][right] - l2r[_r][left - 1]

                ret[r][c] = temp

        return ret
