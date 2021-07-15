class Solution:
     def findPairs(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: int
         """
         
         ### 2 pointers
         # result = 0;
         # nums.sort()
         # for i in range(len(nums) - 1):
         #     if i == 0 or (i != 0 and nums[i] != nums[i - 1]):
         #         for j in range(i + 1, len(nums)):
         #             if nums[j] - nums[i] == k:
         #                 result += 1
         #                 break
         #             elif nums[j] - nums[i] > k:
         #                 break
         # return result
         
         ### map
         result = 0
         c = collections.Counter(nums)
         for i in c:
             if k > 0 and i + k in c or k == 0 and c[i] > 1:
                 result += 1
         return result

