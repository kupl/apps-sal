class Solution:
     def shoppingOffers(self, price, special, needs):
         """
         :type price: List[int]
         :type special: List[List[int]]
         :type needs: List[int]
         :rtype: int
         """
         d = {}
         n = len(needs)
         
         def minp(needs,d):
             if str(needs) in d:
                 return d[str(needs)]
             res = 0
             for i in range(n):
                 res += price[i]*needs[i]
             for s in special:
                 need2 = []
                 for i in range(n):
                     if s[i]>needs[i]:
                         break
                     need2.append(needs[i]-s[i])
                 else:
                     res = min(res, minp(need2,d)+s[-1])
             d[str(needs)] = res
             return res
         
         return minp(needs,d)
