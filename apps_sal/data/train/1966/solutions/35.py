class Solution:
    def countSubMat(self, rowmat: List[int]) -> int:

        length = 0
        count = 0
        for i in range(len(rowmat)):
            length = 0 if rowmat[i] == 0 else (length + 1)
            count += length
        return count

    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0

        for m in range(len(mat)):

            h = [1 for _ in range(len(mat[0]))]
            for down in range(m, len(mat), 1):
                for n in range(len(mat[0])):
                    h[n] = h[n] and mat[down][n]

                count += self.countSubMat(h)

        return count
