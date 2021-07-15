class Solution:
     def calPoints(self, ops):
         """
         :type ops: List[str]
         :rtype: int
         """
         sum = 0
         for i in range (len(ops)):
             op = ops[i]
             if self.isInt(op):
                sum = sum + int(op)
             elif op == 'C':
                 for j in range(i-1 ,-1,-1):
                     if self.isInt(ops[j]):
                         sum = sum - int(ops[j])
                         ops[j] = 'x'
                         break
             elif op == 'D':
                 for j in range(i-1 ,-1,-1):
                     if self.isInt(ops[j]):
                         ops[i] = str(int(ops[j]) * 2)
                         sum = sum + int(ops[i])
                         break
             elif op == '+':
                 for j in range(i-1 , -1,-1):
                     if self.isInt(ops[j]):
                         for k in range(j-1, -1,-1):
                             if self.isInt(ops[k]):
                                 ops[i] = str(int(ops[j]) + int(ops[k]))
                                 sum = sum + int(ops[i])
                                 break
                         break
                         
         return sum
     
     
     def isInt(self,x):
         try:
             return type(int(x)) == int
         except ValueError:
             return False
