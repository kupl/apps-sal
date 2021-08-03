class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myDict = collections.Counter(nums)
        print(myDict)
        for value in list(myDict.values()):
            if value > 1:
                return True
        else:
            return False
