class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k < 1:
            return []
        n1, n2 = len(nums1), len(nums2)
        stack = [(nums1[0] + nums2[0], (0, 0))]
        visited = set()
        res = []
        while len(res) < k and stack:
            num, (p1, p2) = heapq.heappop(stack)
            res.append([nums1[p1], nums2[p2]])
            if p1 + 1 < n1 and (p1 + 1, p2) not in visited:
                heapq.heappush(stack, (nums1[p1 + 1] + nums2[p2], (p1 + 1, p2)))
                visited.add((p1 + 1, p2))
            if p2 + 1 < n2 and (p1, p2 + 1) not in visited:
                heapq.heappush(stack, (nums1[p1] + nums2[p2 + 1], (p1, p2 + 1)))
                visited.add((p1, p2 + 1))
        return res
