class Solution:

    def scan(self, arr, height):
        (_sum, found) = (0, 0)
        for x in arr:
            _sum = 0 if x < height else _sum + 1
            if _sum:
                found += _sum
        return found

    def numSubmat(self, mat: List[List[int]]) -> int:
        (r, result) = (len(mat), 0)
        for i in range(r):
            row = mat[i]
            result += self.scan(row, 1)
            for k in range(i + 1, r):
                row = [x + mat[k][j] for (j, x) in enumerate(row)]
                result += self.scan(row, k - i + 1)
        return result
