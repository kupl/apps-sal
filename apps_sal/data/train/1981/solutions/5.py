class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        interval = defaultdict(int)
        Qs = []
        Qe = []
        for [i, j] in requests:
            heapq.heappush(Qs, i)
            heapq.heappush(Qe, j + 1)
        count = 0
        for i in range(len(nums)):
            while Qs and Qs[0] <= i:
                heapq.heappop(Qs)
                count += 1
            while Qe and Qe[0] <= i:
                heapq.heappop(Qe)
                count -= 1
            interval[i] = count
        keys = sorted(interval, key=lambda x: interval[x], reverse=True)
        values = sorted(nums, reverse=True)
        finala = [0 for i in range(len(nums))]
        j = 0
        for i in keys:
            finala[i] = values[j]
            j += 1
        fsum = 0
        for i in keys:
            fsum += finala[i] * interval[i]
        return fsum % (10 ** 9 + 7)
