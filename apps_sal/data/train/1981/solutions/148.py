class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        reqdict = collections.Counter()
        for request in requests:
            reqdict[request[0]] += 1
            reqdict[request[1] + 1] -= 1

        increments = []
        prev = None
        mult = 0
        for key in sorted(reqdict.keys()):
            #print([key, reqdict[key]])
            if reqdict[key] != 0:
                if prev != None:
                    increments.append([mult, key - prev])
                prev = key
                mult += reqdict[key]

        increments.sort()
        # print(increments)

        x = len(increments) - 1
        ans = 0
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            #print([nums[i], increments[x][0]])
            if x >= 0 and increments[x][0] > 0:
                ans = (ans + nums[i] * increments[x][0]) % (10**9 + 7)

            increments[x][1] -= 1
            if increments[x][1] == 0:
                x -= 1

        return ans
