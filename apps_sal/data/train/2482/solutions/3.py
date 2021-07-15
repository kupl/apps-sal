class Solution:
     def canPlaceFlowers(self, flowerbed, n):
         """
         :type flowerbed: List[int]
         :type n: int
         :rtype: bool
         """
         cnt = 0
         for i, f in enumerate(flowerbed):
             if f == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                 cnt += 1
                 flowerbed[i] = 1
         return cnt >= n
         

