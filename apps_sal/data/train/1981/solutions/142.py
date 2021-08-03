import collections
import heapq


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        heapq.heapify(requests)
        count, end_heap, counter = 0, [], collections.Counter()
        for i in range(len(nums)):
            while requests and i >= requests[0][0]:
                count += 1
                heapq.heappush(end_heap, heapq.heappop(requests)[1])
            while end_heap and i > end_heap[0]:
                heapq.heappop(end_heap)
                count -= 1
            counter[i] += count
        heap = [-num for num in nums]
        heapq.heapify(heap)
        total, mod = 0, 10 ** 9 + 7
        for counts in sorted(list(counter.values()), reverse=True):
            total = (total - heapq.heappop(heap) * counts) % mod
        return total
