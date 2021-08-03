class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # import collections
        # unique_nums = set(nums)
        # count = 0
        # new_nums = collections.Counter(nums)
        # if k == 0:
        #     for i in unique_nums:
        #         if new_nums[i] > 1:
        #             count +=1
        #     return count
        # elif k < 0:
        #     return 0
        # elif k > 0:
        #     for i in unique_nums:
        #         if i+k in unique_nums:
        #             count += 1
        #     return count

# 用counter来做
        # import collections
        # count = 0
        # list_nums = set(nums)
        # if k == 0:
        #     nums = collections.Counter(nums)
        #     for each in nums:
        #         if nums[each] > 1:
        #             count += 1
        #     return count
        # elif k < 0:
        #     return 0
        # elif k > 0:
        #     for i in list_nums:
        #         if i + k in list_nums:
        #             count += 1
        #     return count

# 用dict来做

        count = 0
        if k < 0:
            return count
        if k == 0:
            new_nums = collections.defaultdict(int)
            for i in nums:
                new_nums[i] += 1
            for j in new_nums:
                if new_nums[j] > 1:
                    count += 1
            return count
        if k > 0:
            nums = set(nums)
            for i in nums:
                if i + k in nums:
                    count += 1
            return count

#         if k < 0:
#             return 0
#         if k == 0:
#             dict = collections.defaultdict(int)
#             for i in nums:
#                 dict[i] += 1
#             ans = 0
#             for value in dict.values():
#                 if value > 1:
#                     ans += 1
#             return ans
#         nums = set(nums)
#         ans = 0
#         for item in nums:
#             if item+k in nums:
#                 ans += 1
#         return ans
