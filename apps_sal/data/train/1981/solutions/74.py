class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        d = [0] * len(nums)
        r = defaultdict(int)
        c = 0
        requests.sort()
        j = 0
        for i in range(len(nums)):
            if j >= len(requests):
                d[i] += c
                c -= r[i]
                r[i] = 0
            elif requests[j][0] > i:
                d[i] = c
                c -= r[i]
                r[i] = 0
            else:
                d[i] += c
                c -= r[i]
                r[i] = 0
                while j < len(requests) and requests[j][0] == i:
                    d[i] += 1
                    if requests[j][1] > i:
                        c += 1
                        r[requests[j][1]] += 1
                    j += 1
        #     print(i, c, r)
        # print(requests)
        # print(d)
        ans = 0
        for a, b in zip(sorted(nums, reverse=True), sorted(d, reverse=True)):
            ans += a * b % 1000000007
        return ans % 1000000007

