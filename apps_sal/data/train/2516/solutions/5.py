class Solution:

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap.keys():
                if abs(i - hashmap[nums[i]]) <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
            else:
                hashmap[nums[i]] = i
        return False
