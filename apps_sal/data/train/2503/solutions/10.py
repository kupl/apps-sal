class Solution:
     def findLUSlength(self, a, b):
         """
         :type a: str
         :type b: str
         :rtype: int
         """
         result = 0 
         for i in range(len(a)):
             for j in range(i+1,len(a)+1):
                 if a[i:j] not in b and len(a[i:j])>result:
                     result = len(a[i:j])
         for i in range(len(b)):
             for j in range(i+1,len(b)+1):
                 if b[i:j] not in a and len(b[i:j])>result:
                     result = len(b[i:j])
         if not result:
             return -1
         return result

