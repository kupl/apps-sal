class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        if n <= 1:
            return A
        left = n - 2
        while left >= 0 and A[left] <= A[left + 1]:
            left -= 1
        if left < 0:
            return A
        right = n - 1
        while A[right] >= A[left]:
            right -= 1
        while A[right] == A[right - 1]:
            right -= 1
        (A[left], A[right]) = (A[right], A[left])
        return A
