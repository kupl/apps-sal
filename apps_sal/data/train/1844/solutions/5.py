class Solution:
     def findMinDifference(self, timePoints):
         """
         :type timePoints: List[str]
         :rtype: int
         """
         uniques = set()
         for i in range(len(timePoints)):
             timePoints[i] = int(timePoints[i][:2]) * 60 + int(timePoints[i][-2:])
             if timePoints[i] in uniques:
                 return 0
             uniques.add(timePoints[i])
         uniques.clear()
         
         timePoints.sort()
         minimum = timePoints[0] + 24*60 - timePoints[-1]
         for i in range(1,len(timePoints)):
             temp = timePoints[i] - timePoints[i-1]
             if temp < minimum:
                 minimum = temp
         return minimum
