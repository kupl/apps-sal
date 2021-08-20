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
        for e in intervals:
            if not s:
                a = e[1] - 1
                b = e[1]
                s.add(a)
                s.add(b)
                continue
            if e[0] <= a:
                continue
            if e[0] > a and e[1] > b >= e[0]:
                a = b
                b = e[-1]
                s.add(b)
                continue
            a = e[1] - 1
            b = e[1]
            s.add(a)
            s.add(b)
        return len(s)
