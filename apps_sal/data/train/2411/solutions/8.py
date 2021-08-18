class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
         if len(nums) == 2 or len(nums) == 1:
             return max(nums)
         
         maxes = [nums[0], nums[1], nums[2]]
         maxes.sort() 
         
         for i in range(3, len(nums)):
             pos = self.findPos(nums[i], maxes)
             if pos != None:
                 maxes[pos] = nums[i]
                 
         if maxes[0] == maxes[1] or maxes[1] == maxes[2]:
             return maxes[2]
         else:
             return maxes[0]
                 
     
     def findPos(self, val, maxes):
         maxPos = None
         for ind, aMax in enumerate(maxes):
             if val > aMax:
                 maxPos = ind
             
         return maxPos
         """

        maxes = []

        for i in nums:
            if self.isNew(i, maxes):
                if len(maxes) < 3:
                    maxes.append(i)
                    maxes.sort()
                else:
                    pos = self.findPos(i, maxes)
                    if pos != None:
                        maxes[pos] = i
                        maxes.sort()

        if len(maxes) == 3:
            return maxes[0]
        else:
            return maxes[-1]

    def isNew(self, val, maxes):
        isNew = True
        for i in maxes:
            if val == i:
                isNew = False
        return isNew

    def findPos(self, val, maxes):
        for ind, aMax in enumerate(maxes):
            if val > aMax:
                return ind

        return None
