class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        max_index = -1
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                max_index = max(max_index, i - 1)
        if max_index != -1:
            for i in range(max_index + 1, len(A)):
                if A[i] < A[max_index]:
                    j = i
            A[j], A[max_index] = A[max_index], A[j]
        return A
            

