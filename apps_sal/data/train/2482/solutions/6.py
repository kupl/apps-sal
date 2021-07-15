class Solution:
     def canPlaceFlowers(self, flowerbed, n):
         """
         :type flowerbed: List[int]
         :type n: int
         :rtype: bool
         """
         lenFb = len(flowerbed)
         for i in range(lenFb):
             if i == 0:
                 if flowerbed[i] == 0:
                     if i == lenFb -1:
                         flowerbed[i] = 1
                         n -= 1
                     elif flowerbed[i+1] == 0:
                         flowerbed[i] = 1
                         n -= 1
             elif i == lenFb - 1:
                 if flowerbed[i] == 0:
                     if flowerbed[i-1] == 0:
                         flowerbed[i] = 1
                         n -= 1
             else:
                 if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                     flowerbed[i] = 1
                     n -= 1
         return not (n>0)

