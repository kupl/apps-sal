class Solution:

    def prevPermOpt1(self, A: List[int]) -> List[int]:
        smallestSeenSoFar = A[-1]
        swapOutIndex = -1
        for i in range(len(A) - 2, -1, -1):
            if A[i] > smallestSeenSoFar:
                swapOutIndex = i
                break
            smallestSeenSoFar = min(smallestSeenSoFar, A[i])
        if swapOutIndex == -1:
            return A
        swapInIndex = len(A) - 1
        largestSeenSmallerThanSwapout = 0
        for i in range(len(A) - 1, swapOutIndex, -1):
            if A[i] < A[swapOutIndex] and A[i] >= largestSeenSmallerThanSwapout:
                swapInIndex = i
                largestSeenSmallerThanSwapout = A[i]
        (A[swapOutIndex], A[swapInIndex]) = (A[swapInIndex], A[swapOutIndex])
        return A
