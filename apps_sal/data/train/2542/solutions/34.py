class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3:
            return True
        i = 0
        while i < len(A) - 1 and A[i] == A[i + 1]:
            i += 1
        if i == len(A) - 1:
            return True
        asc = (A[i] < A[i + 1])
        for j in range(i, len(A) - 1):
            if A[j] == A[j + 1]:
                continue
            tmp = (A[j] < A[j + 1])
            if tmp != asc:
                return False
        return True
