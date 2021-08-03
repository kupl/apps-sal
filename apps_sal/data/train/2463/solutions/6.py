class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        N = len(A)
        if N < 3:
            return False
        i = 0
        while i < N - 1:
            if(A[i] < A[i + 1]):
                i += 1
                print(i)
            else:
                break
        if (i == 0 or i == N - 1):
            return False
        while (i < N - 1):
            if (A[i] > A[i + 1]):
                i += 1
                print(i)
            else:
                break
        if(i == N - 1):
            return True
        else:
            return False
