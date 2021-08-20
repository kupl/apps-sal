class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for i in nums:
            if i in hashmap.keys():
                return True
            else:
                hashmap[i] = hash(i)
        return False
