class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        s = [0] * 1440
        for c in timePoints:
            t = (int(c[0]) * 10 + int(c[1])) * 60 + int(c[3]) * 10 + int(c[4])
            if s[t]:
                return 0
            s[t] = 1
        a = []
        for i in range(1440):
            if s[i] == 1:
                a.append(i)
        m = a[0] + 1440 - a[-1]
        for i in range(1, len(a)):
            m = min(m, a[i] - a[i - 1])
        return m
