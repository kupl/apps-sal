class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        my_count = 0
        my_dict = {}
        for n in nums:
            my_count += my_dict.get(n, 0)
            my_dict[n] = my_dict.get(n, 0) + 1
        return my_count
