class Solution:
     def containsNearbyDuplicate(self, nums, k):
         """
         :type nums: List[int]
         :type k: int
         :rtype: bool
         """
         s=set(nums)
         if len(s)==len(nums):return False
         d=dict()
         for num in nums:
             d[num]=d.get(num,0)+1
         for num in d:
             if d[num]>1:
                 index1=-1
                 index2=-1
                 for i in range(len(nums)):
                     if nums[i]==num and index1==-1:index1=i
                     elif nums[i]==num and index2==-1:index2=i
                     elif nums[i]==num and index1!=-1 and index2!=-1:
                         index1=index2
                         index2=i
                     print(index2,index1)
                     if index1!=-1 and index2!=-1 and abs(index2-index1)<=k:return True
         return False
