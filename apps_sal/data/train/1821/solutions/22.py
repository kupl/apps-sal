class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        lst = []
        for x in nums:
            heapq.heappush(lst, x)
        return [heapq.heappop(lst) for x in range(len(nums))]
