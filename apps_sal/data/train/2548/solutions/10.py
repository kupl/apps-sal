class Solution:
     def isUgly(self, num):
         """
         :type num: int
         :rtype: bool
         """
         if num<=0:
             return False
         count=0
         while(count==0):
             num=num/2
             if str(num)[-1]!='0':
                 print(11)
                 count=1
                 num=num*2
         count=0
         while (count==0):
             num=num/3
             if str(num)[-1]!='0':
                 count=1
                 num=num*3        
         count=0
         while (count==0):
             num=num/5
             if str(num)[-1]!='0':
                 count=1
                 num=num*5
         if num!=1.0:
             return False
         else:
             return True
