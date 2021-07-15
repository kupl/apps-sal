class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                break
        
        if A[i] <= A[i+1]:
            return A
        max_j = 0
        j_ind = i
        for j in range(i, len(A)):
            if A[i] > A[j]:
                max_j = max(max_j, A[j])
                if max_j == A[j]:
                    j_ind = j
        
        # swap
        tmp = A[i]
        A[i] = A[j_ind]
        A[j_ind] = tmp
        return A
        
        

