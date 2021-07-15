class Solution:
     def calculate(self, s):
         """
         :type s: str
         :rtype: int
         """
         
         if not s:
             return 0
         
         digits = '0123456789'
         stack = [0]
         pre_op = '+'
         cur_num = 0
         s += '#'
         
         for c in s:
             if c == ' ':
                 continue
                 
             if c in digits:
                 cur_num = cur_num * 10 + int(c)
                 continue
                 
             if pre_op == '-':
                 cur_num *= -1
             elif pre_op == '*':
                 cur_num *= stack.pop()
             elif pre_op == '/':
                 if cur_num == 0:
                     return None
                 
                 pre_num = stack.pop()
                 flag = 1 if pre_num > 0 else -1
                 cur_num = abs(pre_num) // cur_num * flag
                 
             stack.append(cur_num)
             pre_op = c
             cur_num = 0
             
         return sum(stack)
         

