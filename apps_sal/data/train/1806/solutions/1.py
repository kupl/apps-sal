from collections import Counter
 
 class Poly():
     def __init__(self,v):
         self.c = Counter()
         self.c[''] = 0
         
         if isinstance(v,int):
             self.c[''] = v
         elif isinstance(v,str):
             self.c[v] = 1
         elif isinstance(v,Counter):
             self.c = v
     
     def __add__(self,other):
         cn = Counter()
         for el,c in self.c.items():
             cn[el] += c
         for el, c in other.c.items():
             cn[el] += c
         return Poly(cn)
     
     def __sub__(self,other):
         cn = Counter()
         for el,c in self.c.items():
             cn[el] += c
         for el, c in other.c.items():
             cn[el] -= c
         return Poly(cn)
     
     def __mul__(self,other):
         cn = Counter()
         for el1, v1 in self.c.items():
             for el2, v2 in other.c.items():
                 #print(el1.split('*'))
                 sn = '*'.join(sorted(it for it in el1.split('*')+el2.split('*') if it != ''))
                 cn[sn] += v1*v2
         return Poly(cn)
     
     def toList(self):
         vet = []
         def comp(key):
             el = key[0]
             v = [it for it in el.split('*') if it != '']
             return (-len(v),v)
         
         for el,v in sorted(self.c.items(), key = comp):
             #print(len(el),el,v)
             if v == 0:
                 continue
             
             vap = [str(v)]
             vap += [it for it in el.split('*') if it != '']
             #print(vap)
             vet.append('*'.join(vap))
         
         return vet
     
     def __str__(self):
         return str(self.c)
 
 def rfind(vet,v):
     for i in range(len(vet)-1,-1,-1):
         if vet[i] == v:
             return i
     return -1
 
 class Solution:
     def basicCalculatorIV(self, expression, evalvars, evalints):
         """
         :type expression: str
         :type evalvars: List[str]
         :type evalints: List[int]
         :rtype: List[str]
         """
         
         valToInt = dict(zip(evalvars,evalints))
         self.i = 0
         def parse():
             parsed = []
             while self.i < len(expression):
                 ch = expression[self.i]
                 if ch.isalpha():
                     s = ''
                     while self.i < len(expression) and expression[self.i].isalpha():
                         s += expression[self.i]
                         self.i += 1
                     parsed.append(s if s not in valToInt else valToInt[s])
                 elif ch.isdigit():
                     s = ''
                     while self.i < len(expression) and expression[self.i].isdigit():
                         s += expression[self.i]
                         self.i += 1
                     parsed.append(int(s))
                 elif ch in '+-*':
                     self.i += 1
                     parsed.append(ch)
                 elif ch == '(':
                     self.i += 1
                     parsed.append(parse())
                 elif ch == ')':
                     self.i += 1
                     return parsed
                 else:
                     self.i += 1
             return parsed
         
         parsed = parse()
         
         def polyPlus(vet):
             if '+' in vet:
                 i = vet.index('+')
                 #print(polyPlus(vet[:i])+polyPlus(vet[i+1:]))
                 return polyPlus(vet[:i])+polyPlus(vet[i+1:])
             return polyMinus(vet)
         
         def polyMinus(vet):
             if '-' in vet:
                 i = rfind(vet,'-')
                 #print(polyMinus(vet[:1])-polyMinus(vet[2:]))
                 return polyMinus(vet[:i])-polyMinus(vet[i+1:])
             return polyTimes(vet)
         
         def polyTimes(vet):
             if '*' in vet:
                 i = vet.index('*')
                 return polyTimes(vet[:i])*polyTimes(vet[i+1:])
             return polyElement(vet)
         
         def polyElement(vet):
             if len(vet) == 0:
                 return Poly(None)
             assert len(vet) == 1
             el = vet[0]
             if isinstance(el,list):
                 return polyPlus(el)
             return Poly(el)
             
         polyAns = polyPlus(parsed)
         ans = polyAns.toList()
         return ans

