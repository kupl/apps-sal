class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i in range(len(nums)):
            l = d.get(nums[i], [])
            if nums[i] in d:
                for j in l:
                    if abs(i - j) <= k:
                        return True
            l.append(i)
            d[nums[i]] = l

        return False
