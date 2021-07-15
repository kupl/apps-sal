class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests.sort()
        ct = []
        heap = []
        for i in range(len(nums)):
            while len(requests) != 0 and requests[0][0] == i:
                heapq.heappush(heap, requests[0][1])
                requests.pop(0)
            while len(heap) != 0 and heap[0] < i:
                heapq.heappop(heap)
            ct.append(len(heap))
        ct.sort(reverse=True)
        nums.sort()
        j = ans = 0
        for i in range(len(nums) - 1, -1, -1):
            ans += nums[i] * ct[j]
            j += 1
        return ans % (10 ** 9 + 7)
