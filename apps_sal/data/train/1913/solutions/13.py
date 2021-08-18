class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                break
        if A[i] <= A[i + 1]:
            return A
        j = max([x for x in range(i, len(A)) if A[x] < A[i]], key=lambda x: A[x])
        A[i], A[j] = A[j], A[i]
        return A
