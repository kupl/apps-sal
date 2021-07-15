class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase, decrease = True, True
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                decrease = False
            if A[i] < A[i - 1]:
                increase = False
        return increase or decrease
