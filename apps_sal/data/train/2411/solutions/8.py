class Solution:

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '\n         if len(nums) == 2 or len(nums) == 1:\n             return max(nums)\n         \n         maxes = [nums[0], nums[1], nums[2]]\n         maxes.sort() # ascending\n         \n         for i in range(3, len(nums)):\n             pos = self.findPos(nums[i], maxes)\n             if pos != None:\n                 maxes[pos] = nums[i]\n                 \n         if maxes[0] == maxes[1] or maxes[1] == maxes[2]:\n             return maxes[2]\n         else:\n             return maxes[0]\n                 \n     \n     def findPos(self, val, maxes):\n         maxPos = None\n         for ind, aMax in enumerate(maxes):\n             if val > aMax:\n                 maxPos = ind\n             \n         return maxPos\n         '
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
        for (ind, aMax) in enumerate(maxes):
            if val > aMax:
                return ind
        return None
