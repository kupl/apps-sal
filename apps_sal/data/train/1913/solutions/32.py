class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 2, -1, -1):
            for x in range(len(A) - 1, i, -1):
                if A[x] == A[x - 1]:
                    continue
                if A[i] > A[x]:
                    A[i], A[x] = A[x], A[i]
                    return A
        return A
