class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        tracker = {}

        for num in nums:
            if num not in tracker:
                tracker[num] = 0
            else:
                tracker[num] += 1

        sum = 0
        for num in tracker:
            sum += tracker[num] * (tracker[num] + 1) // 2
        return sum
