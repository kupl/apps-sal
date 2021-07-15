class Solution:
     def timetominute(self, time1):
         t1 = int(time1[:2]) * 60 + int(time1[3:5])
         return t1
     def findMinDifference(self, timePoints):
         """
         :type timePoints: List[str]
         :rtype: int
         """
         count = 1440
         for i in range(len(timePoints)):
             timePoints[i] = self.timetominute(timePoints[i])
         timePoints.sort(reverse = False)
         print(timePoints)
         for i in range(len(timePoints)):
             if (timePoints[(i + len(timePoints)) % len(timePoints) - 1] - timePoints[(i + 1 + len(timePoints)) % len(timePoints) -1]) < 0:
                 count = min(min((timePoints[(i + 1 + len(timePoints)) % len(timePoints) -1] - timePoints[(i + len(timePoints)) % len(timePoints) - 1]), (timePoints[(i + len(timePoints)) % len(timePoints) - 1] - (timePoints[(i + 1 + len(timePoints)) % len(timePoints) -1 ] ) + 1440)),count)
             else:
                 count = min(min((timePoints[(i + len(timePoints)) % len(timePoints) - 1] - timePoints[(i + 1 + len(timePoints)) % len(timePoints) -1]), (timePoints[(i + 1 + len(timePoints)) % len(timePoints) -1] - timePoints[(i + len(timePoints)) % len(timePoints) - 1] + 1440)),count)
         return count

