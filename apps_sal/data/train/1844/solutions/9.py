def minDifference(minsA, minsB):
     maxMins = 60 * 24
     earlier = min(minsA, minsB)
     later = max(minsA, minsB)
     direct = later - earlier
     loopAround = maxMins - later + earlier
     return min(direct, loopAround)
 
 def toMinutes(timeString):
     h = int(timeString.split(":")[0])
     m = int(timeString.split(":")[1])
     return m + h * 60
 
 class Solution:
     def findMinDifference(self, timePoints):
         """
         :type timePoints: List[str]
         :rtype: int
         """
         # timePoints.sort()
         # currentMin = 60 * 24 + 1
         # for i in range(-1, len(timePoints) - 1):
         #     currentMin = min(currentMin, minDifference(toMinutes(timePoints[i]), toMinutes(timePoints[i+1])))
         # return currentMin
         minBuckets = [None] * (24 * 60)
         for i in range(24 * 60):
             minBuckets[i] = False
             
         for time in timePoints:
             if minBuckets[toMinutes(time) - 1] == True:
                 return 0
             minBuckets[toMinutes(time) - 1] = True
             
         last = None
         maxTime = 0
         minTime = 24 * 60 + 1
         minDistance = 24 * 60 + 1
         for i in range(24 * 60):
             if last == None and minBuckets[i] == True:
                 first = i
                 last = i
             elif minBuckets[i] == True:
                 minDistance = min(minDistance, i - last)
                 last = i
                 veryLast = i
         minDistance = min(minDistance, 24 * 60 - veryLast + first)
         return minDistance
         
         
                 
             
