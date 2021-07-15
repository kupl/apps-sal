class Solution:
     def isOneBitCharacter(self, bits):
         """
         :type bits: List[int]
         :rtype: bool
         """
         n=len(bits)
         flag=[0 for i in range(n)]
         i=0
         while i <n-1:
             print(i)
             if bits[i]==1:
                 flag[i+1]=1
             i=i+1+flag[i+1]
         result=True if flag[-1]==0 else False
         return result

