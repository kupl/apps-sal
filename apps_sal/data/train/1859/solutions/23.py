from itertools import accumulate
from typing import List

def transpose(m):
    return list(map(list, zip(*m)))

def prefix_sums(m):
    return [list(accumulate(r)) for r in m]


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        bsums = transpose(prefix_sums(transpose(prefix_sums(matrix))))
        squares = 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                k = 0
                while i + k < m and j + k < n:
                    s = bsums[i+k][j+k]
                    if i > 0: s -= bsums[i -1][j + k]
                    if j > 0: s -= bsums[i + k][j - 1]
                    if i > 0 and j > 0: s += bsums[i - 1][j - 1]
                    if s == (k + 1) ** 2:
                        squares += 1
                    else:
                        break
                    k += 1
        return squares
