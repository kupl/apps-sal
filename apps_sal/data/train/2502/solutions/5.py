class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         #空或这有一个，不卖
         
         if len(prices) < 2:
             return 0
         #初始化一个最大值，其实只要最后一个数比倒数第二个数大，就可以产生  最后一个数与倒数第#二数的差值的。不管最后一次在什么时候卖的
         max1 = 0
         for i in range(1,len(prices)):
             print(max1)
             max1 += max(0,prices[i] - prices[i-1])
         return max1
         
             
         
         
             
         

