class Solution:
     def complexNumberMultiply(self, a, b):
         """
         :type a: str
         :type b: str
         :rtype: str
         """
         ca = self.toTuple(a)
         cb = self.toTuple(b)
         return self.fromTuple(self.multiply(ca, cb))
         
     def toTuple(self, a):
         index = a.index('+')
         return int(a[:index]), int(a[index+1: -1])
     
     def fromTuple(self, a):
         return '{}+{}i'.format(a[0], a[1])
     
     def multiply(self, a, b):
         return a[0] * b[0] - a[1] * b[1], a[1] * b[0] + a[0] * b[1]

