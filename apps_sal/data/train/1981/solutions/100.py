class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        events = []
        for s, e in requests:
            events.append((s, \"a\"))
            events.append((e, \"b\"))
        events.sort()
        ne = len(events)
        depth, stabs = 0, []
        event_i = 0
        x, kind = events[0]
        for i in range(len(nums)):
            while x <= i and kind == \"a\" and event_i < ne:
                depth += 1
                event_i += 1
                if event_i >= ne: break
                x, kind = events[event_i]
            stabs.append(depth)
            while x <= i and kind == \"b\" and event_i < ne:
                depth -= 1
                event_i += 1
                if event_i >= ne: break
                x, kind = events[event_i]
        stabs.sort(reverse = True)
        nums.sort(reverse = True)
        ans = 0
        for freq, val in zip(stabs, nums):
            ans += freq*val
            ans %= MOD
        return ans % MOD
        
