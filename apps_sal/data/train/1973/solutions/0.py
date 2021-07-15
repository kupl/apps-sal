class Solution:
     def isIdealPermutation(self, A):
         """
         :type A: List[int]
         :rtype: bool
         """
         # tle
         # for i in range(len(A)-2):
             # if A[i] > min(A[i+2:]):
                 # return False
         # return True
                 
         # ac
         for i in range(len(A)):
             if abs(A[i] - i) > 1:
                 return False
         return True
