class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        requests.sort(reverse = True)
        counts = []
        ends = []
        curr = 0
        for i in range(N):
            while requests and requests[-1][0] == i:
                s, e = requests.pop()
                curr += 1
                heapq.heappush(ends, e)
            counts.append(curr)
            while ends and ends[0] == i:
                heapq.heappop(ends)
                curr -= 1
                
        res = 0
        for v, c in zip(sorted(counts), sorted(nums)):
            res += v * c
        return res % (10**9+7)

