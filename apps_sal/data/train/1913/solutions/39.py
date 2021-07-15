class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        if not A:
            return []
        
        i = len(A) - 1
        # find first elt A[i - 1] > A[i], from right to left
        # 1[9]467, find 9
        #   i
        while i > 0 and A[i - 1] <= A[i]:
            i -= 1
        if i == 0:
            return A # already at the smallest permutation
        
        # 1[9]46[7], find first elt < A[i - 1], which is 7
        # swap 9 and 7
        j = len(A) - 1
        while j > i and A[j] >= A[i - 1]:
            j -= 1
        
        
        while j >= i and A[j] == A[j - 1]:
            j -= 1
        
        A[j], A[i - 1] = A[i - 1], A[j]
        return A
        

