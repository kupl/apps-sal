class Solution(object):
    def rectangleArea(self,rectangles):
        events = []
        MOD = 10**9 + 7
        INT_MIN = -2 **32
        for x1, y1, x2, y2 in rectangles:
            events.append([x1, 0, y1, y2])
            events.append([x2, 1, y1, y2])
        events.sort()

        def merge_intervals(m,intervals):
            l = 0 
            n = len(intervals)
            if n == 0:
                return 0 
            prev = intervals[0]
            l = prev[1]-prev[0]
            print (intervals,l,m)
            prev_end = prev[1]
            for s,t in intervals[1:]:
                if s>=prev_end:
                    l += t-s
                else:
                    if t > prev_end:
                        l = l + (t-s) - (prev_end-s)
                prev_end = max(t,prev_end) 
            return l*m
                
        def gain_area(m):
            area = 0
            prev = INT_MIN
            for l, r in open_intervals:
                prev = max(prev, l)
                area += max(0, (r - prev))
                prev = max(r, prev)
            print (\"gain area\",area,open_intervals)
            return area*m
        
        area = 0
        prev = INT_MIN
        open_intervals = []
        for event in events:
            curr,close,y1,y2 = event
            print (curr,prev,curr-prev)
            area += merge_intervals(curr-prev,open_intervals)
            gain_area(curr-prev)
            if close:
                open_intervals.remove((y1,y2))
            else:
                open_intervals.append((y1,y2))
                open_intervals.sort()
            prev = curr
        return area  % MOD
