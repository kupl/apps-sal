class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        canPlant = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                canPlant += 1
                flowerbed[0] = 1
        else:
            for i in range(len(flowerbed)):
                if flowerbed[i] == 0:
                    if i == 0:
                        if flowerbed[i + 1] == 0:
                            flowerbed[i] = 1
                            canPlant += 1
                    elif i == len(flowerbed) - 1:
                        if flowerbed[i - 1] == 0:
                            flowerbed[i] = 1
                            canPlant += 1
                    else:
                        if flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                            flowerbed[i] = 1
                            canPlant += 1
        if canPlant >= n:
            return True
        else:
            return False
