class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        q = [intervals[0][1]]
        counter = 0
        for a,b in intervals[1:]:
            t = [x for x in q]
            flag = 0
            for v in q:
                if a > v:
                    t.remove(v)
                    flag = 1
                elif b <= v:
                    counter += 1
                    break
                else:
                    flag = 1
            if flag == 1:
                t.append(b)
            q = t
        return len(intervals) - counter
        

