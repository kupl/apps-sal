class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        d = [0] * len(nums)
        r = [0] * len(nums)
        c = 0
        j = 0
        requests.sort()
        for i in range(len(nums)):
            d[i] += c
            c -= r[i]
            r[i] = 0
            while j < len(requests) and requests[j][0] == i:
                d[i] += 1
                if requests[j][1] > i:
                    c += 1
                    r[requests[j][1]] += 1
                j += 1
                    
        ans = 0
        for a, b in zip(sorted(nums, reverse=True), sorted(d, reverse=True)):
            if not b:
                break
            ans += a * b % 1000000007
        return ans % 1000000007

