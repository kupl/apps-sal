'''
 # Brute Force
 class Solution:
     def isIdealPermutation(self, A):
         """
         :type A: List[int]
         :rtype: bool
         """
         countGlobal = 0
         countLocal = 0
         for i in range(len(A)):
             for j in range(i+1, len(A)):
                 if A[i] > A[j]:
                     countGlobal += 1
         
         for i in range(len(A)-1):
             if  A[i] > A[i+1]:
                 countLocal += 1
         
         if countLocal == countGlobal:
             return True
         else:
             return False
 '''     
 class Solution:
     def isIdealPermutation(self, A):
         for i in range(len(A)):
             if abs(A[i]-i) >= 2:
                 return False
         return True
         
