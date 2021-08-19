class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        '\n        from end, find 1st number which is greater than atleast 1 no. from its right\n        \n        '
        (i, mn, mx) = (n - 2, n - 1, n - 1)
        while i >= 0:
            if A[i] > A[mn]:
                mx = i
            if A[i] < A[mn]:
                mn = i
            if mn != mx and mx < mn:
                break
            i -= 1
        if i == -1:
            return A
        print((mx, mn))
        mxR = mx + 1
        for j in range(mx + 1, n):
            if A[j] < A[mx] and A[j] > A[mxR]:
                mxR = j
        (A[mx], A[mxR]) = (A[mxR], A[mx])
        return A
