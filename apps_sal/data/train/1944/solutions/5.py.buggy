import re
 class Solution:
     def solveEquation(self, equation):
         """
         :type equation: str
         :rtype: str
         """
         # Gets sum of x's in an eq
         def get_x_sum(s):
 
             total = 0
             curr = ""
             sign = "+"
             for c in s:
                 if c == "x":
                     if curr == "":
                         total += int(sign+"1")
                     else:
                         total += int(sign+curr)
                 elif c == "+" or c == "-":
                     curr = ""
                     sign = c
                 else:
                     curr += c
             
             return total
         
         # Gets sum of ints in an eq
         def get_int_sum(s):
             total = 0
             curr = ""
             sign = "+"
             for c in s:
                 if c == "x":
                     curr = ""
                     sign = "+"
                 elif c == "+" or c == "-":
                     if curr != "":
                         total += int(sign+curr)
                         curr = ""
                     sign = c
                 else:
                     curr += c
             
             if curr != "":
                 total += int(sign+curr)
             return total
             
         lhs,rhs = equation.split("=")
         
         lhs_sum_x = get_x_sum(lhs)
         lhs_sum_int = get_int_sum(lhs)
         rhs_sum_x = get_x_sum(rhs)
         rhs_sum_int = get_int_sum(rhs)
         
         if lhs_sum_int == rhs_sum_int:
             if lhs_sum_x == rhs_sum_x:
                 return "Infinite solutions"
             return "x=0"
         else:
             if lhs_sum_x == rhs_sum_x:
                 return "No solution"
             
             diff_x = lhs_sum_x-rhs_sum_x
             diff_int = rhs_sum_int - lhs_sum_int
             return "x=" + str(diff_int // diff_x)
             
             
         
         
         

