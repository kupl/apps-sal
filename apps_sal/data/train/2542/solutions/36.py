class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        def isIncreasing(self, A: List[int]) -> bool:
            mono = True
            for i in range(len(A)):
                if i == (len(A) - 1):
                    break
                if A[i] > A[i+1]:
                    mono = False
            return mono
        def isDecreasing(self, A: List[int]) -> bool:
            m = True
            for i in range(len(A)):
                if i == (len(A) - 1):
                    break
                if A[i] < A[i+1]:
                    m = False
            return m
        if isDecreasing(self,A) or isIncreasing(self,A):
            return True
        return False
            

