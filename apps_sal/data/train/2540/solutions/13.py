import numpy as np


class Solution:

    def largestPerimeter(self, A: List[int]) -> int:

        def valid_area(x, y, z): return True if x < y + z else False
        A = sorted(A, reverse=True)
        for a in range(2, len(A)):
            if valid_area(A[a - 2], A[a - 1], A[a]):
                return np.sum([A[a - 2], A[a - 1], A[a]])
        return 0
