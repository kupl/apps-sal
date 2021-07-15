class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        requests.sort(reverse=True)
        cur = []
        height = []
        for i in range(len(nums)):
            while requests and requests[-1][0] <= i:
                heapq.heappush(cur, requests.pop()[1])
            while cur and cur[0] < i:
                heapq.heappop(cur)
            height.append(len(cur))
        print(height)
        height.sort()
        nums.sort()
        return sum(n * h for n, h in zip(nums, height)) % (10 ** 9 + 7)


