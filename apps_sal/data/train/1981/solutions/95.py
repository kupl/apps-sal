class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = (10 ** 9 + 7)

        events = []
        for l, r in requests:
            events.append((l, 1))
            events.append((r + 1, -1))
        events.sort()

        request_counts = [0 for i in range(len(nums))]
        j = 0
        total = 0
        for i in range(len(request_counts)):
            while j < len(events) and events[j][0] == i:
                total += events[j][1]
                j += 1
            request_counts[i] = total

        request_counts.sort()
        nums.sort()

        result = 0
        for r, n in zip(request_counts, nums):
            result = (result + r * n) % MOD

        return result
