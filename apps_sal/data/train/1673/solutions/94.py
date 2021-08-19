from typing import List
from functools import lru_cache


class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        (m, n) = (len(arr), len(arr[0]))

        @lru_cache(None)
        def helper(r, c):
            if r == m:
                return 0
            return arr[r][c] + min((helper(r + 1, nc) for nc in range(n) if nc != c))
        return min((helper(0, c) for c in range(n)))
