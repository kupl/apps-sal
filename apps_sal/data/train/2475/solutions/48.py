class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        for i in range(len(A)):
            self.convertCharsToIntArray(i,A)
            
        counts = 0
        for i in range(len(A[0])):
            checker = False
            for j in range(1,len(A)):
                if A[j-1][i] > A[j][i]:
                    checker = True
            if checker:
                counts += 1
        return counts 
        
    def convertCharsToIntArray(self,i,A):
        chars = A[i]
        array = []
        for char in chars:
            array.append(ord(char))
        A[i] = array

