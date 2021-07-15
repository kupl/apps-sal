class Solution:
     def myAtoi(self, str):
         """
         :type str: str
         :rtype: int
         """
         str = str.strip()
         if len(str)==0: return 0
         
         if str[0] =="-":
             ret, i = 0, 1
             sign = -1
         elif str[0] == "+":
             ret, i = 0, 1
             sign = 1
         else:
             ret, i = 0, 0
             sign =1
         while i < len(str) and str[i].isdigit() :
             ret = ret*10 + int(str[i])
             i += 1
         return max(-2**31, min(sign * ret,2**31-1))
