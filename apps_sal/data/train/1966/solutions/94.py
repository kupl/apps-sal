class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        right_ct = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            ct = 0
            for j in range(len(mat[0]) - 1, -1, -1):
                if mat[i][j] == 1:
                    ct += 1
                else:
                    ct = 0
                right_ct[i][j] = ct

        res = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                right_min = float('inf')
                for k in range(i, len(mat)):
                    right_min = min(right_min, right_ct[k][j])
                    res += right_min

        return res
