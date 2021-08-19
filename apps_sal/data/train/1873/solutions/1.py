class Solution:

    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end) or start.replace('X', '') != end.replace('X', ''):
            return False
        (l, ll, r, rr) = (0, 0, 0, 0)
        for i in range(len(start)):
            if start[i] == 'L':
                l += 1
            elif start[i] == 'R':
                r += 1
            if end[i] == 'L':
                ll += 1
            elif end[i] == 'R':
                rr += 1
            if l > ll or r < rr:
                return False
        return True
