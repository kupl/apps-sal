class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tlen = len(timePoints)
        if tlen < 2:
            return 0
        arr = [0] * tlen
        for i in range(tlen):
            h, m = timePoints[i].split(':')
            arr[i] = int(h) * 60 + int(m)
        arr.sort()
        minx = float('inf')
        for i in range(1, tlen):
            if minx > arr[i] - arr[i - 1]:
                minx = arr[i] - arr[i - 1]
        if minx > arr[0] + 24 * 60 - arr[-1]:
            minx = arr[0] + 24 * 60 - arr[-1]
        return minx
