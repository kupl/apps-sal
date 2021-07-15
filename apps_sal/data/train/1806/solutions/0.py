
 import re
 
 
 class Solution:
     def calc(self, a, b, op):
         if op == '+':
             for k, v in b.items():
                 a[k] = a.get(k, 0) + v
             return a
         elif op == '-':
             for k, v in b.items():
                 a[k] = a.get(k, 0) - v
             return a
         elif op == '*':
             t = {}
             for k1, v1 in a.items():
                 for k2, v2 in b.items():
                     t[tuple(sorted(k1+k2))] = t.get(tuple(sorted(k1+k2)), 0) + v1 * v2
             return t
 
     def basicCalculatorIV(self, expression, evalvars, evalints):
         vars = {n:v for n,v in zip(evalvars, evalints)}
         d = []  # operands
         op = []
         priority = {'(': 0, '+': 1, '-': 1, '*': 2}
         for t in re.findall(r'\(|\)|[a-z]+|[0-9]+|[\+\-\*]', expression):
             if t[0].isdigit():
                 d.append({tuple():int(t)})
             elif t[0].isalpha():
                 if t in vars:
                     d.append({tuple():vars[t]})
                 else:
                     d.append({(t,): 1})
             elif t == '(':
                 op.append(t)
             elif t == ')':
                 while op and op[-1] != '(':
                     d.append(self.calc(d.pop(-2), d.pop(-1), op.pop()))
                 op.pop()
             elif t in '+-*':
                 if not op or priority[t] > priority[op[-1]]:
                     op.append(t)
                 else:
                     while op and priority[t] <= priority[op[-1]]:
                         d.append(self.calc(d.pop(-2), d.pop(-1), op.pop()))
                     op.append(t)
         while op:
             d.append(self.calc(d.pop(-2), d.pop(-1), op.pop()))
 
         res = []
         for k in sorted(d[0].keys(), key=lambda x: (-len(x), x)):
             v = d[0][k]
             if v != 0:
                 if not k:
                     res.append(str(v))
                 else:
                     res.append('%s*%s' % (v, '*'.join(k)))
         return res

