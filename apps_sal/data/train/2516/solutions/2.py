class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}

        for i, n in enumerate(nums):
            if n in m and abs(m[n] - i) <= k:
                return True
            m[n] = i

        return False

    '''
     Ex testcase: [1,2,3,4,5,6,7,1,9,1] k = 3
     '''
