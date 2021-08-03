class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        pairs = {}

        cnt = 0

        for a in nums:
            if not a in pairs:
                if a + k in pairs and a not in pairs[a + k]:
                    pairs[a + k].append(a)
                    cnt += 1
                if a - k in pairs and a not in pairs[a - k]:
                    pairs[a - k].append(a)
                    cnt += 1
                pairs[a] = []
            else:
                if not a + k in pairs[a]:
                    if a + k in pairs and a not in pairs[a + k]:
                        pairs[a + k].append(a)
                        cnt += 1
                if not a - k in pairs[a]:
                    if a - k in pairs and a not in pairs[a - k]:
                        pairs[a - k].append(a)
                        cnt += 1

        return cnt
