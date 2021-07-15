import re
 
 class Solution:
     def complexNumberMultiply(self, a, b):
         """
         :type a: str
         :type b: str
         :rtype: str
         """
         pattern = r"-?\d+"
         l1 = list(map(int, re.findall(pattern, a)))
         l2 = list(map(int, re.findall(pattern,b)))
         whole = (l1[0] * l2[0]) - (l1[1] * l2[1])
         comp = (l1[0] * l2[1]) + (l2[0] * l1[1])
         return (str(whole) + '+' + str(comp)+ 'i')
         
