class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        (a1, a2) = (sorted(A), sorted(A, reverse=True))
        if A == a1 or A == a2:
            return True
        return False
        '\n        nD, nI = 1, 1\n        for i in range(1, len(A)):\n            if A[i] - A[i-1] < 0:\n                nD = 0\n            elif A[i] - A[i-1] > 0 :\n                nI = 0\n        return nI or nD\n        '
