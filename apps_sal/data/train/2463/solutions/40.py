class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        N = len(A)-1
        i = 0

        # walk up
        while i < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N:
            return False

        # walk down
        while i < N and A[i] > A[i+1]:
            i += 1

        return i == N

