class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good = 0
        num_dict = {}
        for num in nums:
            if num in num_dict:
                good += num_dict[num]
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        return good
