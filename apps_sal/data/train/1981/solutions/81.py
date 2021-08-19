class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)

        events = []
        OPEN = -1
        CLOSE = 1
        for u, v in requests:
            events.append([u, OPEN])
            events.append([v, CLOSE])
        events.sort()
        weights = [0] * n

        open_events = 0
        nxt_event = 0

        for i in range(n):
            # open here
            while nxt_event < len(events) and events[nxt_event][0] <= i:
                if events[nxt_event][1] == OPEN:
                    open_events += 1
                else:
                    break
                nxt_event += 1
            # compute weight
            weights[i] = open_events
            # close here
            while nxt_event < len(events) and events[nxt_event][0] <= i:
                if events[nxt_event][1] == CLOSE:
                    open_events -= 1
                nxt_event += 1

        return sum([w * num for w, num in zip(sorted(weights), sorted(nums))]) % MOD
