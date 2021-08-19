class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # interval_set = set(tuple(interval) for interval in intervals)
        # to_remove = set()
        # for a, b in interval_set:
        #     if (a, b) not in to_remove:
        #         for c, d in interval_set:
        #             if not (a==c and b==d) and (c, d) not in to_remove and a <= c and b >= d:
        #                 to_remove.add((c, d))
        # return len(interval_set) - len(to_remove)
        mx = max(list(map(max, intervals)))
        max_from = [0] * mx
        for a, b in intervals:
            max_from[a] = max(max_from[a], b)

        # print(max_from)
        mx = 0
        for i in range(len(max_from)):
            mx = max(mx, max_from[i])
            max_from[i] = mx
        # print(max_from)

        cnt = len(intervals)
        for a, b in intervals:
            if max_from[a] > b or (a > 0 and max_from[a - 1] >= b):
                cnt -= 1
        return cnt
