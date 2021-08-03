class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if len(timePoints) > 1440:
            return 0
        timeNum = [0] * len(timePoints)
        for i in range(len(timePoints)):
            timeNum[i] = 60 * int(timePoints[i][:2]) + int(timePoints[i][3:])

        timeNum.sort()
        minMin = 24 * 60
        for i in range(len(timeNum) - 1):
            minMin = min(minMin, timeNum[i + 1] - timeNum[i])
        minMin = min(minMin, 24 * 60 + timeNum[0] - timeNum[-1])
        return minMin
