class Solution:
     def countOfAtoms(self, formula):
         """
         :type formula: str
         :rtype: str
         """
         dict = self.helper(formula)
         result = ""
         for key in sorted(dict):
             result += str(key) + (str(dict[key]) if dict[key] > 1 else "")
         return result
     
     def helper(self, formula):
         result = {}
         j = 0 # conventional i, j are reversed
         element = ""
         while j < len(formula):
             if formula[j] == "(":
                 if len(element) > 0:
                     result[element] = (result[element] if element in result else 0) + 1
                     element = ""
                 count = 1
                 end = j + 1
                 while end < len(formula) and count > 0:
                     if formula[end] == "(":
                         count += 1
                     if formula[end] == ")":
                         count -= 1
                     end += 1
                 dict = self.helper(formula[j + 1: end - 1])
                 i = end 
                 while i < len(formula) and formula[i].isdigit():
                     i += 1
                 m = int(formula[end: i])
                 for key, value in list(dict.items()):
                     result[key] = value * m + (result[key] if key in result else 0)
             elif formula[j].isdigit():
                 i = j + 1
                 while i < len(formula) and formula[i].isdigit():
                     i += 1
                 result[element] = (result[element] if element in result else 0) + int(formula[j:i])
                 element = ""
             else:
                 if len(element) > 0:
                     result[element] = (result[element] if element in result else 0) + 1
                     element = ""
                 i = j + 1
                 while i < len(formula) and formula[i].islower():
                     i += 1
                 element = formula[j:i]
             j = i
         if not formula[j - 1].isdigit():
             result[element] = (result[element] if element in result else 0) + 1
         return result
 

