class Solution:
     def canPlaceFlowers(self, flowerbed, n):
         """
         :type flowerbed: List[int]
         :type n: int
         :rtype: bool
         """
         result = False
         if n == 0:
             return True
         if flowerbed:
             if len(flowerbed) == 1:
                 if flowerbed[0] == 0:
                     flowerbed[0] = 1
                     n -= 1
                     return n == 0
             for i in range(len(flowerbed)):
                 left, right = False, False
                 if flowerbed[i] == 0 and n != 0:
                     if i == 0 and len(flowerbed) >= 2:
                         if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                             flowerbed[i] = 1
                             n -= 1
                     else:
                         left = i - 1 >= 0 and flowerbed[i - 1] == 0 
                     
                     if i == len(flowerbed) - 1 and len(flowerbed) >= 2:
                         if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                             flowerbed[i] =1 
                             n -= 1
                     else:
                         right = i + 1 < len(flowerbed) and flowerbed[i + 1] == 0
                     
                     if left and right:
                         flowerbed[i] = 1
                         n -= 1
             result = (n == 0)
         return result
