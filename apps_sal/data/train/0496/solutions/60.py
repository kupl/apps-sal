class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        A_sum = sum(A)
        cnt = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                cnt += (A[i] - A[i - 1] + 1)
                
                A[i] = A[i - 1] + 1
        return sum(A) - A_sum
