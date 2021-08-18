class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]

        COORDINATE COMPRESSION IS THE WAY TO GO - CHECKOUT OFFICAL LEETCODE ANSWER.  THIS WORKS TOO.
        """

        ints = []
        for left, size in positions:
            ints.append(left)
            ints.append(left + size - 1)

        index = {num: idx for idx, num in enumerate(sorted(ints))}
        heights = [0] * 2 * len(positions)

        def query(left, right):
            return max(heights[index[left]: index[right] + 1])

        def updateHeights(left, right, newheight):
            for i in range(index[left], index[right] + 1):
                heights[i] = newheight

        maxheights = []
        for left, size in positions:
            right = left + size - 1
            newheight = query(left, right) + size
            updateHeights(left, right, newheight)
            if not maxheights or maxheights[-1] <= newheight:
                maxheights.append(newheight)
            else:
                maxheights.append(maxheights[-1])

        return maxheights
