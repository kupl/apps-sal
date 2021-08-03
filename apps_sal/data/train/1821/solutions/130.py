import heapq


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapify(nums)
        new = []

        while nums:
            new.append(heappop(nums))
        return new
