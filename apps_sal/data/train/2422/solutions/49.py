class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        m1 = heapq.heappop(heap)
        m2 = heapq.heappop(heap)

        return -(m1 + 1) * -(m2 + 1)
