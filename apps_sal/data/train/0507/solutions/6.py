class Solution:
     def singleNonDuplicate(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         #return sum(set(nums))*2-sum(nums)
         '''
         one = 0
         for num in nums:
             one = (~one&num)|(one&~num)
         return one
         '''
         l, r = 0, len(nums)-1
         while l < r:
             mid = (l+r)//2
             if nums[mid] == nums[mid-1]:
                 if (r-mid)%2 == 1:
                     l = mid + 1
                 else:
                     r = mid - 2
             elif nums[mid] == nums[mid+1]:
                 if (mid-l)%2 == 1:
                     r = mid - 1
                 else:
                     l = mid + 2
             else:
                 return nums[mid]
         return nums[l]

