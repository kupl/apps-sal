from functools import lru_cache
from itertools import product


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])

        @lru_cache(None)
        def leftsum(i, j):
            if j < 0 or mat[i][j] == 0:
                return 0
            return 1 + leftsum(i, j - 1)

        ret = 0

        for bottom, j in product(list(range(R)), list(range(C))):
            width = j + 1
            for top in range(bottom, -1, -1):
                width = min(leftsum(top, j), width)
                if width == 0:
                    break
                ret += width

        return ret
