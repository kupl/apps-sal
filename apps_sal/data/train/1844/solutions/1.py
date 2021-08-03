class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i in range(len(timePoints)):
            t = timePoints[i]
            h = ''
            m = ''
            deb = True
            for j in range(len(t)):
                if t[j] == ':':
                    deb = False
                elif deb:
                    h += t[j]
                else:
                    m += t[j]
            timePoints[i] = int(m) + 60 * int(h)

        timePoints.sort()
        print(timePoints)
        mi = float("inf")
        for i in range(len(timePoints) - 1):
            diff = timePoints[i + 1] - timePoints[i]
            if diff < mi:
                mi = diff
        last = (24 * 60 - timePoints[-1]) + timePoints[0]
        if last < mi:
            mi = last
        return mi
