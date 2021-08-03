class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        possible = 0
        repeated = 1

        for f in flowerbed:
            if f:
                if repeated:
                    possible += (repeated - 1) // 2
                repeated = 0
            else:
                repeated += 1

        if repeated:
            possible += repeated // 2

        return (possible >= n)
