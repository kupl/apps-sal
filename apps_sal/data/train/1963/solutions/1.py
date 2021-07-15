class Solution:
     def shoppingOffers(self, price, special, needs):
         """
         :type price: List[int]
         :type special: List[List[int]]
         :type needs: List[int]
         :rtype: int
         """
         #用一个局部的最小值，每次更新
         def directPurchase(price,needs):
             total=0
             for i in range(len(needs)):
                 total+=price[i]*needs[i]
             return total
         #index表示对special offer遍历
         def dfs(price,special,needs,index):
             #一种在现实中有可能发生的情况：单独买可能比买套餐更加便宜
             local_min=directPurchase(price,needs)
             for i in range(index,len(special)):
                 offer=special[i]
                 temp=[]
                 #如果买了某种商品，则needs的数量一直更新,needs是个数组，所以需要遍历
                 for j in range(len(needs)):
                     #需要的比提供的少，不满足“刚好”的条件
                     if needs[j]<offer[j]:
                         #这一句很重要，不然会报错，只要有一种产品不满足条件，这一个special就都不能买
                         temp=[]
                         break
                     else:
                         #需要的更多
                         temp.append(needs[j]-offer[j])
                 #如果还有需要买的东西
                 if temp!=[]:
                     #动态规划的过程
                     local_min=min(local_min,offer[-1]+dfs(price,special,temp,i))
             return local_min
         return dfs(price,special,needs,0)
                         

