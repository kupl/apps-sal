class Solution:
     def complexNumberMultiply(self, a, b):
         """
         :type a: str
         :type b: str
         :rtype: str
         """
         (A, B) = self.parse_complex(a)
         (C, D) = self.parse_complex(b)
         return "%d+%di" % (A * C - B * D, A * D + B * C)
 
     def parse_complex(self, content):
         [a, b] = content.split('+')
         return int(a), int(b[:-1])
