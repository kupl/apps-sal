class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 1, 0, -1):
            if A[i - 1] > A[i]:
                break
        if i == 1 and A[i - 1] <= A[i]:
            return A
        j = max([x for x in range(i, len(A)) if A[x] < A[i - 1]], key=lambda x: A[x])
        (A[i - 1], A[j]) = (A[j], A[i - 1])
        return A
