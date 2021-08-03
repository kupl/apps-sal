class Solution:
    def pourWater(self, heights, total, index):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """

        if not heights or total <= 0 or index < 0 or index >= len(heights):
            return heights

        for _ in range(total):
            left = -1
            for i in range(index - 1, -1, -1):
                if heights[i] > heights[i + 1]:
                    break

                if heights[i] < heights[i + 1]:
                    left = i

            if left != -1:
                heights[left] += 1
                continue

            right = -1
            for j in range(index + 1, len(heights)):
                if heights[j] > heights[j - 1]:
                    break

                if heights[j] < heights[j - 1]:
                    right = j

            if right != -1:
                heights[right] += 1
                continue

            heights[index] += 1

        return heights
