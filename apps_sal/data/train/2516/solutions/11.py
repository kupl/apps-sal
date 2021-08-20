class Solution:

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        from collections import defaultdict
        dup_idx = defaultdict(list)
        for (i, num) in enumerate(nums):
            dup_idx[num].append(i)
        for idxes in dup_idx.values():
            if len(idxes) == 1:
                continue
            idxes = sorted(idxes)
            for i in range(1, len(idxes)):
                if idxes[i] - idxes[i - 1] <= k:
                    return True
        return False
