class Solution:

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        temp = 0
        m = 0
        if flowerbed[0] == 0:
            temp = 1
        for (i, plot) in enumerate(flowerbed):
            if plot == 0:
                temp += 1
                if i == len(flowerbed) - 1:
                    temp += 1
            if plot == 1 or i == len(flowerbed) - 1:
                m += int((temp - 1) / 2)
                temp = 0
            if m >= n:
                return True
        return False
