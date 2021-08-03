class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        left = n - 1
        while left >= 1 and A[left - 1] <= A[left]:
            left -= 1
        if left == 0:
            return A
        right = left
        left = left - 1
        for i in range(right, n):
            if A[i] > A[right] and A[i] < A[left]:
                right = i
        A[left], A[right] = A[right], A[left]
        return A
