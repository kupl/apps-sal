class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return A

        for i in range(len(A) - 1, 0, -1):
            if A[i - 1] > A[i]:
                m, mi = A[i], i
                for j in range(i, len(A)):
                    if A[j] < A[i - 1] and A[j] > m:
                        mi = j
                        m = A[j]
                A[i - 1], A[mi] = A[mi], A[i - 1]
                break
        return A
