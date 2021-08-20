class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        events = []
        for (s, e) in requests:
            events.append((s, 1))
            events.append((e + 1, -1))
        events.sort()
        n = len(nums)
        request_count = [0] * n
        count = 0
        i = 0
        for j in range(n):
            while i < len(events) and j == events[i][0]:
                count += events[i][1]
                i += 1
            request_count[j] = count
        request_count.sort()
        nums.sort()
        result = 0
        while request_count and request_count[-1] > 0:
            result += request_count.pop() * nums.pop()
        return result % 1000000007
