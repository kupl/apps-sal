class Solution:
    def specialArray(self, nums: List[int]) -> int:
        len_num = len(nums)
        for x in range(1, len_num+1):
            elem_greater = 0
            for num in nums:
                elem_greater += num >= x
            if x == elem_greater:
                return x
        return -1
