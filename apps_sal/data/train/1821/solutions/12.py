class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import heapq
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        sorted_list = []
        while heap:
            sorted_list.append(heapq.heappop(heap))
        return sorted_list
