class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        l = -1
        for i in reversed(range(len(A) - 1)):
            if A[i] > A[i + 1]:
                l = i
                break
        if l >= 0:
            r = l + 1
            s = A[r]
            for i in range(l + 2, len(A)):
                if A[i] < A[l] and A[i] >= s:
                    r = i
            (A[l], A[r]) = (A[r], A[l])
        return A
