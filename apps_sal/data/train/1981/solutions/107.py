class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requestCount = defaultdict(int)
        begHeap = []
        endHeap = []
        for req in requests:
            heapq.heappush(begHeap, req[0])
            heapq.heappush(endHeap, req[1] + 1)
        poppedCount = 0
        for i in range(len(nums)):
            while begHeap and begHeap[0] <= i:
                heapq.heappop(begHeap)
                poppedCount += 1
            while endHeap and endHeap[0] <= i:
                heapq.heappop(endHeap)
                poppedCount -= 1
                continue
            requestCount[i] = poppedCount
        sortedRequest = sorted(list(requestCount.items()), key=lambda x: -x[1])
        nums.sort(key=lambda x: -x)
        out = 0
        for (n, s) in zip(nums, sortedRequest):
            out += n * s[1]
        return out % (pow(10, 9) + 7)
