MODULO = 10**9 + 7


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        events = [0] * len(nums)
        for s, e in requests:
            events[s] += 1
            if e + 1 < len(nums):
                events[e + 1] -= 1

        for i in range(1, len(events)):
            if events[i] == 0:
                events[i] = events[i-1]
            else:
                events[i] = events[i-1] + events[i]

        print(events)

        events.sort()
        nums.sort()

        summa = 0
        for v, n in zip(events, nums):
            summa = (summa + v * n) % MODULO
        return summa

