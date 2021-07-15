class Solution:
     def isIdealPermutation(self, A):
         """
         :type A: List[int]
         :rtype: bool
         """
         max_value = A[0]
         for i in range(1,len(A)-1):
             if A[i+1] < max_value:
                 return False
             if A[i] > max_value:
                 max_value = A[i]
         else:
             return True
         # local_count = 0
         # global_count = 0
         # for i in range(len(A)-1):
         #     if A[i] > A[i+1]:
         #         local_count += 1
         #     for j in range(len(A)):
         #         if A[i] > A[j] and i < j:
         #             global_count += 1
         # return local_count == global_count

