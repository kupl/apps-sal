class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        idx = -1
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                idx = i

        if idx == -1:
            return A

        for i in range(len(A) - 1, idx, -1):
            if A[i] < A[idx] and A[i] != A[i - 1]:
                A[idx], A[i] = A[i], A[idx]
                break
        return A
