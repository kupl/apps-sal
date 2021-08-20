class Solution:

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        seen = set([])
        import heapq
        min_heap = []
        max_number = nums[0]
        for num in nums:
            if num not in seen:
                max_number = max(max_number, num)
                seen.add(num)
                if len(min_heap) == 3:
                    if min_heap[0] < num:
                        heapq.heappop(min_heap)
                    else:
                        continue
                heapq.heappush(min_heap, num)
        if len(min_heap) < 3:
            return max_number
        return heapq.heappop(min_heap)
