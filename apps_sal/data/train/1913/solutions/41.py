class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        
        # Start from the right, see if any values are smaller than current index
        
        smallestSeenSoFar = A[-1]
        
        swapOutIndex = -1
        for i in range(len(A) - 2, -1, -1):
            
            if A[i] > smallestSeenSoFar:
                # We can perform a swap on this index
                swapOutIndex = i
                break
            
            smallestSeenSoFar = min(smallestSeenSoFar, A[i])
        
        if swapOutIndex == -1:
            # We cannot swap out any values, so we terminate
            return A
        
        # Now, we need to find the largest index smaller than the swapout index
        swapInIndex = len(A) - 1
        largestSeenSmallerThanSwapout = 0
        
        for i in range(len(A) - 1, swapOutIndex, -1):
            
            if A[i] < A[swapOutIndex] and A[i] >= largestSeenSmallerThanSwapout:
                swapInIndex = i
                largestSeenSmallerThanSwapout = A[i]
                # We also choose the highest index that is matching our criterion
        
        # Now we found the swap in index, we perform the swap
        
        A[swapOutIndex], A[swapInIndex] = A[swapInIndex], A[swapOutIndex]
        
        return A
