class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        H = mat
        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if H[i][j] == 0:
                    continue
                H[i][j] = H[i - 1][j] + 1
        total = 0
        for i in range(len(H)):
            for j in range(len(H[0])):
                if H[i][j] == 0:
                    continue
                h = H[i][j]
                total += h
                for k in range(j + 1, len(H[0])):
                    if H[i][k] == 0:
                        break
                    h = min(H[i][k], h)
                    total += h
        return total
