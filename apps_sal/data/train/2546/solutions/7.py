class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        uniques = set(nums)
        count = 0
        for unique in uniques:
            count += nums.count(unique) * (nums.count(unique) - 1) / 2
        return int(count)
