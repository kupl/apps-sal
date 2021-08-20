class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        i = len(A) - 2
        while i >= 0 and A[i + 1] >= A[i]:
            i -= 1
        if i == -1:
            return A
        k = i + 1
        j = i + 1
        while j < len(A):
            if A[k] < A[j] < A[i]:
                k = j
            j += 1
        (A[i], A[k]) = (A[k], A[i])
        return A
