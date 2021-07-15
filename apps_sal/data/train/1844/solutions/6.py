class Solution:
     def convertToInt(self, time):
         hours = int(time.split(':')[0])
         mins = int(time.split(':')[1])
         return 60*hours+mins
 
     def findMinDifference(self, timePoints):
         """
         :type timePoints: List[str]
         :rtype: int
         """
         s = set()
         for time in timePoints:
             mins = self.convertToInt(time)
             if mins in s:
                 return 0
             else:
                 s.add(mins)
         
         result = 12*60
         s = sorted(s)
         N = len(s)
         prev = s[N-1] - 24*60
         for i in range(N):
             if s[i] - prev < result:
                 result = s[i] - prev
             prev = s[i]
         return result
             
             

