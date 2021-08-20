class Solution:

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        L = len(flowerbed)
        if n > (L + 1) // 2:
            return False
        if L == 1:
            return flowerbed[0] == 0
        (cnt, i) = (0, 0)
        while i < L:
            if flowerbed[i] == 1:
                i += 2
            elif i < L - 1 and flowerbed[i + 1] == 1:
                i += 3
            elif i == L - 1:
                cnt += int(flowerbed[i - 1] == 0)
                i += 1
            elif i == 0 or flowerbed[i - 1] == 0:
                cnt += 1
                i += 2
        return cnt >= n
