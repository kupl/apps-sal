class Solution:

    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for i in range(V):
            if not self.fallLeft(K, heights):
                if not self.fallRight(K, heights):
                    heights[K] += 1
        return heights

    def fallLeft(self, K, heights):
        minBlock = K
        for i in range(K - 1, -1, -1):
            if heights[i] < heights[minBlock]:
                minBlock = i
            elif heights[i] > heights[minBlock]:
                break
        if minBlock == K:
            return False
        heights[minBlock] += 1
        return True

    def fallRight(self, K, heights):
        minBlock = K
        for i in range(K + 1, len(heights)):
            if heights[i] < heights[minBlock]:
                minBlock = i
            elif heights[i] > heights[minBlock]:
                break
        if minBlock == K:
            return False
        heights[minBlock] += 1
        return True
