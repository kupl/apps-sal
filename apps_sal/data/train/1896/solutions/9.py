class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        queue = []
        heapq.heappush(queue, [nums1[0] + nums2[0], 0, 0])
        ans = []
        seen = {(0, 0): 1}
        while k > len(ans) and queue:
            top = heapq.heappop(queue)
            i, j = top[1], top[2]
            ans.append([nums1[i], nums2[j]])
            #print(i, j, queue)
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(queue, [nums1[i + 1] + nums2[j], i + 1, j])
                seen[(i + 1, j)] = 1
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(queue, [nums1[i] + nums2[j + 1], i, j + 1])
                seen[(i, j + 1)] = 1
        return ans
