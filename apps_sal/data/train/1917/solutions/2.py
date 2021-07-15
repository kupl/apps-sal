class Solution:
     def countOfAtoms(self, formula):
         """
         :type formula: str
         :rtype: str
         """
         stack = []
         mapping = collections.defaultdict(int)
         s = ""
         num = 0
         i = 0
         while i < len(formula):
             c = formula[i]
             if c.islower():
                 s += c
                 i += 1
             elif c.isdigit():
                 num = 10 * num + int(c)
                 i += 1
             else:
                 if num == 0:
                     num = 1
                 if s != "":
                     mapping[s] += num
                 s = ""
                 num = 0
                 i += 1
                 if c.isupper():
                     s = c
                 elif c == '(':
                     stack.append(mapping)
                     mapping = collections.defaultdict(int)
                 elif c == ')':
                     while i < len(formula) and formula[i].isdigit():
                         num = 10 * num + int(formula[i])
                         i += 1
                     prev = stack.pop()
                     for k in mapping:
                         prev[k] += mapping[k] * num
                     mapping = prev
                     num = 0
         if num == 0:
             num = 1
         if s != "":
             mapping[s] += num
         ans = []
         for k, v in sorted(mapping.items()):
             ans.append(k)
             if v > 1:
                 ans.append(str(v))
         return ''.join(ans)

