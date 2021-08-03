class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count, pos = 0, 0
        while pos < len(flowerbed):
            if (pos - 1 < 0 or not flowerbed[pos - 1]) and \
                (not flowerbed[pos]) and \
                    (pos + 1 > len(flowerbed) - 1 or not flowerbed[pos + 1]):
                print(pos)
                count += 1
                pos += 2
            else:
                pos += 1
        return count >= n
