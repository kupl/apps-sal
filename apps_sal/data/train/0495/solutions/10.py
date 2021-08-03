class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        self.dp = {}

        def helper(index, total):

            if index == len(stones):
                return abs(total)

            if (index, total) in self.dp:
                return self.dp[(index, total)]

            self.dp[(index, total)] = min(helper(index + 1, total + stones[index]), helper(index + 1, total - stones[index]))
            return self.dp[(index, total)]

        return helper(0, 0)
