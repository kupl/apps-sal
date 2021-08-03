class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def helper(i, currSum):
            if i == len(stones):
                return abs(total - 2 * currSum)
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            takeIt = helper(i + 1, currSum + stones[i])
            ignoreIt = helper(i + 1, currSum)
            cache[(i, currSum)] = min(takeIt, ignoreIt)
            return cache[(i, currSum)]

        cache = {}
        total = sum(stones)
        return helper(0, 0)
