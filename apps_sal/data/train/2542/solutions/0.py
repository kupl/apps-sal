class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A: return True
        increasing = True
        index = 0
        while index<len(A)-1 and A[index] == A[index+1]:
            index+=1
        if index == len(A)-1:
            return True
        if A[index] > A[index+1]:
            increasing = False
        for i in range(len(A)-1):
            if increasing:
                if A[i] > A[i+1]:
                    return False
            else:
                if A[i] < A[i+1]:
                    return False
        return True
