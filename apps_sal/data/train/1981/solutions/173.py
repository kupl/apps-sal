class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        reqBounds = []
        for i in range(0, len(requests)):
            reqBounds.append((requests[i][0], 1))
            reqBounds.append((requests[i][1] + 1, -1))
        reqBounds = sorted(reqBounds, key=lambda x: (x[0], -x[1]))
        weight, curW, prev = [], 0, 0
        for i in range(0, len(reqBounds)):
            if reqBounds[i][1] == 1:
                weight.append((curW, reqBounds[i][0] - prev))
                curW += 1
                prev = reqBounds[i][0]
            else:
                weight.append((curW, reqBounds[i][0] - prev))
                curW -= 1
                prev = reqBounds[i][0]
        weight = sorted(weight, key=lambda x: -x[0])
        nums = sorted(nums, key=lambda x: -x)
        k, ans = 0, 0
        for i in range(0, len(weight)):
            for j in range(0, weight[i][1]):
                ans += weight[i][0] * nums[k]
                k += 1
        return ans % (10**9 + 7)
