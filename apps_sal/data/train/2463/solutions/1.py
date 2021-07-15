class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        isIncreasing = True
        i = 1
        n = len(A)
        if n < 3:
            return False
        if A[1] <= A[0]:
            return False
        while i < n:
            if isIncreasing and A[i-1] < A[i]:
                i += 1
                continue
            elif A[i] < A[i-1]:
                isIncreasing = False
                i += 1
                continue
            else:
                return False
        if A[-1] >= A[-2]:
            return False
        return True
