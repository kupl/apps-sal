class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if A == sorted(A):
            return A
        idx = None
        for i in range(len(A) - 1, 0, -1):
            if A[i - 1] > A[i]:
                idx = i - 1
                break
        mx = float('-inf')
        for i in range(idx + 1, len(A)):
            if mx < A[i] < A[idx]:
                mx = A[i]
                midx = i
        (A[midx], A[idx]) = (A[idx], A[midx])
        return A
