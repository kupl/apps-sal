class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0

        for i in range(len(mat)):
            row = [1 for _ in range(len(mat[0]))]
            for j in range(i, len(mat)):
                for k in range(len(mat[0])):
                    row[k] &= mat[j][k]
                res += self.countRow(row)

        return res

    def countRow(self, row: List[int]) -> int:
        res = length = 0

        for i, val in enumerate(row):
            length = 0 if val == 0 else length + 1
            res += length

        return res
