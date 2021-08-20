class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        (res, map) = (0, {})
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                res += map[num]
                map[num] += 1
        return res
