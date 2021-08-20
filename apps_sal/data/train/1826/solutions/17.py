class Solution:

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat) - 1
        n = len(mat[0]) - 1
        row = []
        lookup = {}
        for (i, r) in enumerate(mat):
            col = []
            for (j, c) in enumerate(mat[0]):
                area = ((0 if i - K < 0 else i - K, 0 if j - K < 0 else j - K), (m if i + K > m else i + K, n if j + K > n else j + K))
                key = str(area)
                if key not in lookup:
                    lookup[key] = self.matrixBlockSumHelp(mat, area)
                col += [lookup[key]]
            row += [col]
        return row

    def matrixBlockSumHelp(self, mat, area):
        ((a, b), (c, d)) = area
        return sum([sum(row[b:d + 1]) for row in mat[a:c + 1]])
