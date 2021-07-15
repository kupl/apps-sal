class Solution:
     def toHex(self, num):
         """
         :type num: int
         :rtype: str
         """
         if num==0:
             return "0"
         res,n=[],0
         nums=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
         while n<8 and num!=0:
             res.insert(0,nums[num%16])
             num=num//16
             n+=1
         s=""
         for i in res:
             s+=i
         return s

