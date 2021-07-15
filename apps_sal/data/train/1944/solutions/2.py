class Solution:
     def solveEquation(self, equation):
         l, r = equation.split("=")
         ret = self.compute(l)
         lnum, lx = ret[0], ret[1]
         ret = self.compute(r)
         rnum, rx = ret[0], ret[1]
         if lx == rx and lnum - rnum == 0:
             return "Infinite solutions"
         elif lx == rx and lnum - rnum != 0:
             return "No solution"
         else:
             if rx > lx:
                 return "x=" + str(int((lnum - rnum)/(rx - lx)))
             else:
                 return "x=" + str(int((rnum - lnum)/(lx - rx)))
             
         print((lx, lnum))
         
     def compute(self, eq):
         val = ''
         s = '+'
         eq =  eq + '+'
         num, x = 0,0
         for c in eq:
             if c == 'x':
                 if val == '':
                     val = '1'
                 if s =='+':
                     x += int(val)
                 else:
                     x -= int(val)
                 val = ''
             elif c == '+' or c == '-':
                 if val != '' and s == '+':
                     num += int(val)
                 elif val != '' and s == '-':
                     num -= int(val)
                 s = c
                 val = ''
 
             else:
                 val += c
         return num, x

