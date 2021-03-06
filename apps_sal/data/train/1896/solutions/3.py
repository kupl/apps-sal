class Solution:

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        queue = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        while queue and len(ans) < k:
            (_, i, j) = heapq.heappop(queue)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < len(nums1):
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))
        return ans
