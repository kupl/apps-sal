class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        q = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(q, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        res = []
        while q and len(res) < k:
            s, i, j = heapq.heappop(q)
            res.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return res
