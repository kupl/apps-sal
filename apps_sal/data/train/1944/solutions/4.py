class Solution:
     def solveEquation(self, equation):
         """
         :type equation: str
         :rtype: str
         """
         count_x = count_integer = 0
         left, right = equation.replace('-', ' -').replace('+', ' +').split('=')
         left_items = left.lstrip().split(' ')
         right_items = right.lstrip().split(' ')
         for l in left_items:
             if l[-1] == 'x':
                 if l[:-1] == '' or l[:-1] == '+':
                     count_x += 1
                 elif l[:-1] == '-':
                     count_x -= 1
                 else:
                     count_x += int(l[:-1])
             else:
                 count_integer -= int(l)
         for r in right_items:
             if r[-1] == 'x':
                 if r[:-1] == '' or r[:-1] == '+':
                     count_x -= 1
                 elif r[:-1] == '-':
                     count_x += 1
                 else:
                     count_x -= int(r[:-1])
             else:
                 count_integer += int(r)
         if count_x == 0 and count_integer != 0:
             return 'No solution'
         elif count_x == 0 and count_integer == 0:
             return 'Infinite solutions'
         else:
             return 'x=' + str(int(count_integer / count_x))

