class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        temp = None
        for i in A:
            if i == temp:
                return i
            temp = i
            
        if A[0] == A[-2] or A[0] == A[-1]:
            return A[0]
        elif  A[-1] == A[-3]:
            return A[-1]
