class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        events = []
        r = 0
        for i in range(0, len(intervals)):
            events.append([i, intervals[i][0], 0, intervals[i][1]])
            events.append([i, intervals[i][1], 1, intervals[i][0]])
        events.sort(key=lambda x: (x[1], -x[3]))
        ai = []
        po = {}
        for i in range(0, len(events)):
            if events[i][2] == 0:
                po[events[i][0]] = list(ai)
                ai.append(events[i][0])
            else:
                if not list(set(po[events[i][0]]) & set(ai)):
                    r += 1
                ai.remove(events[i][0])
        return r
