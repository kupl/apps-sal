class Solution:
     def findShortestSubArray(self, nums):
         
         diction = {}
         
         for i in nums:
             if i not in diction:
                 diction[i] = 1
             else:
                 diction[i] += 1
             
         degree = max(list(diction.values()))
         
         if degree == 1:
             return 1
         
         max_value = []
         
         for i in diction:
             if diction[i] == degree:
                 max_value.append(i)
         
         min_length = 10000000000
         
         for i in max_value:
             head = 0
             tail = 0
             for j in range(len(nums)):
                 if nums[j] == i:
                     head = j
                     break
             for j in range(len(nums)-1,-1,-1):
                 if nums[j] == i:
                     tail = j
                     break
             if min_length > tail - head + 1:
                 min_length = tail - head + 1
         
         return min_length
