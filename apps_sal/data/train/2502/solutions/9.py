class Solution:
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         # 7 2 3 4 1 5 3 4
         # 7 3 2 1 5 7 9 4 5
         if len(prices) < 2:
             return 0
         buy = prices[0] #1
         sell = -1
         profit = 0
         i = 1
         while i < len(prices):
             if buy >= prices[i]:
                 if sell> -1:
                     profit += sell-buy #15
                     sell = -1
                     buy = prices[i] # 2
                 else:
                     buy = prices[i] #1
             if prices[i] > buy:
                 if prices[i] > sell:
                     sell = prices[i] #9
                 else:
                     profit+=sell - buy #
                     sell = -1 
                     buy = prices[i] #2
                     
             
             i+=1
         if sell>-1:
             profit+=sell - buy
         return profit

