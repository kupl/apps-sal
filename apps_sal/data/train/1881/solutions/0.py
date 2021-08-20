class Solution:

    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        if len(intervals) <= 1:
            return len(intervals[0])
        s = set()
        prev_e = None
        intersect = False
        for e in intervals:
            if not s:
                a = e[1] - 1
                b = e[1]
                s.add(a)
                s.add(b)
                continue
            if e[0] <= a:
                intersect = True
                continue
            if e[0] > a and e[1] > b >= e[0]:
                intersect = True
                a = b
                b = e[-1]
                s.add(b)
                continue
            a = e[1] - 1
            b = e[1]
            s.add(a)
            s.add(b)
        if not intersect:
            return 0
        return len(s)
