class Solution:
     def countOfAtoms(self, formula):
         """
         :type formula: str
         :rtype: str
         """
         
         def merge(d1, d2):
             for k, v in list(d2.items()):
                 if k in d1:
                     d1[k] += v
                 else:
                     d1[k] = v
                     
         def mul(d, multiplier):
             for k in list(d.keys()):
                 d[k] *= multiplier
                 
         def helper(start):
             c = formula[start]
             els = {}
             end = start
             if c == '(':
                 end += 1
                 while formula[end] != ')':
                     end, els2 = helper(end)
                     merge(els, els2)
                 end += 1
             elif 'A' <= c <= 'Z':
                 end += 1
                 while end < len(formula) and 'a' <= formula[end] <= 'z':
                     end += 1
                 els[formula[start:end]] = 1
             else:
                 raise ValueError('Unexpected token')
                 
             end2 = end
             while end2 < len(formula) and '0' <= formula[end2] <= '9':
                 end2 += 1
             count = int(formula[end:end2]) if end2 != end else 1
             mul(els, count)
             return end2, els
         
         
         i, result = helper(0)
         while i < len(formula):
             i, els = helper(i)
             merge(result, els)
             
         keys = sorted(result.keys())
         s = ""
         for k in keys:
             if result[k] > 1:
                 s+="%s%d"%(k, result[k])
             else:
                 s+=k
         return s
         
             

