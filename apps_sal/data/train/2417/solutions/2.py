class Solution:
     def convertToBase7(self, num):
         flag = 0
         if num < 0:
             num = -num
             flag = 1
         elif num == 0:
             return "0"
         temp = num;
         #str1 = ""
         list1 = []
         while temp > 0:
             num = temp % 7
             temp = temp // 7
             list1.insert(0, str(num))
         if flag == 1:
             list1.insert(0, "-")
         str1 = "".join(list1)
         return str1
 

