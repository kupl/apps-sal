class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        result = 0
        nums.sort()
        n = len(nums)
        LARGE = int(1000000000.0 + 7)
        events = []
        for re in requests:
            events.append([re[0], 1])
            events.append([re[1] + 1, -1])
        events.sort()
        prev = -1
        result = 0
        index = 0
        count = [-1 for i in range(n + 1)]
        now = 0
        for (num, change) in events:
            now += change
            count[num] = now
        for i in range(n):
            if count[i] == -1:
                if i == 0:
                    count[i] = 0
                else:
                    count[i] = count[i - 1]
        count.pop()
        count.sort()
        return sum([count[i] * nums[i] for i in range(n)]) % LARGE
