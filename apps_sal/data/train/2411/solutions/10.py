class Solution:

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_list = [None] * 3
        max_list[0] = nums[0]
        for num in nums[1:]:
            print(max_list)
            if num > max_list[0]:
                max_list[2] = max_list[1]
                max_list[1] = max_list[0]
                max_list[0] = num
            if max_list[1]:
                if max_list[0] > num > max_list[1]:
                    max_list[2] = max_list[1]
                    max_list[1] = num
                if max_list[2]:
                    if max_list[1] > num > max_list[2]:
                        max_list[2] = num
                elif max_list[1] > num:
                    max_list[2] = num
            elif max_list[0] > num:
                max_list[1] = num
        return max_list[2] if max_list[2] is not None else max_list[0]
