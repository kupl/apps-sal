import heapq


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        sorted_nums = []
        while heap:
            cur_min = heapq.heappop(heap)
            sorted_nums.append(cur_min)
        return sorted_nums
