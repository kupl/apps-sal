class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        (inc, dec) = (True, True)
        for i in range(1, len(A)):
            (a, b) = (A[i], A[i - 1])
            inc = inc & (a >= b)
            dec = dec & (a <= b)
            if not (inc or dec):
                return False
        return inc or dec
