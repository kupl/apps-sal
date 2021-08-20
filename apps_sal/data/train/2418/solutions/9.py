class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myDict = {}
        for num in nums:
            if myDict.get(num):
                return True
            else:
                myDict[num] = 1
        else:
            return False
