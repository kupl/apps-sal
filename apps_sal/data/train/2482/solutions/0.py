class Solution:
     def canPlaceFlowers(self, flowerbed, n):
         """
         :type flowerbed: List[int]
         :type n: int
         :rtype: bool
         """
         p = flowerbed.count(1)
         m = int(len(flowerbed) / 2)
         if p+n <= m+1:
             pos = 0
             while pos < len(flowerbed):
                 if n == 0:
                     print(n)
                     return True
                 else:
                     if pos+1 < len(flowerbed):
                         if flowerbed[pos] == 0 and flowerbed[pos+1] == 0:
                             print(pos)
                             n-=1
                             pos+=2
                         elif flowerbed[pos] == 1:
                             pos += 2
                         else:
                             pos +=3
                     else:
                         if flowerbed[pos] == 0:
                             n-=1
                             pos+=2
             if n == 0:
                 return True
             else:
                 return False
         else:
             return False
