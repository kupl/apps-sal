from heapq import heappop, heappush


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        h = []
        result = []
        for num in nums:
            heappush(h, num)
        while h:
            result.append(heappop(h))
        return result
