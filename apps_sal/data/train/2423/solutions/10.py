class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # return -min(0, min(accu for accu in itertools.accumulate(nums))) + 1
        return 1 - min(accumulate(nums, initial=0))
