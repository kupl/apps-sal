class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if not A:
            return []
        i = len(A) - 1
        while i > 0 and A[i - 1] <= A[i]:
            i -= 1
        if i == 0:
            return A
        j = len(A) - 1
        while j > i and A[j] >= A[i - 1]:
            j -= 1
        while j >= i and A[j] == A[j - 1]:
            j -= 1
        (A[j], A[i - 1]) = (A[i - 1], A[j])
        return A
