class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        l = len(A) - 2
        while l >= 0:
            if A[l + 1] < A[l]:
                break
            l -= 1
        max_so_far = 0
        max_idx = l
        r = l + 1
        while r < len(A):
            if A[r] > max_so_far and A[r] < A[l]:
                max_so_far = A[r]
                max_idx = r
            r += 1
        if 0 <= l <= max_idx < len(A):
            A[l], A[max_idx] = A[max_idx], A[l]
        return A
