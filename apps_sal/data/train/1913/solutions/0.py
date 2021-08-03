class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        if n == 1:
            return A

        tidx = -1
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                tidx = i
                break

        if tidx < 0:
            return A

        sidx = -1
        for j in range(n - 1, tidx, -1):
            if A[j] == A[j - 1]:
                continue
            if A[j] < A[tidx]:
                sidx = j
                break

        A[tidx], A[sidx] = A[sidx], A[tidx]

        return A
