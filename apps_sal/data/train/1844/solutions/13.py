class Solution:
     def to_minutes(self, timePoints): # if in place
         ret_list = []
         for hour in timePoints:
             h, m = tuple(map(int, hour.split(':')))
             
             m += h*60
             ret_list.append(m)
         
         return ret_list
             
             
     def findMinDifference(self, timePoints):
         """
         :type timePoints: List[str]
         :rtype: int
         """
         minutes_p = self.to_minutes(timePoints)
         
         minutes_p.sort()
         
         min_minutes = 1439 # distance from 00:00 to 23:59
         for i in range(len(minutes_p)-1):
             if i == 0:
                 min_minutes = min(abs(minutes_p[i]-minutes_p[i-1]+1440),min_minutes)
             min_minutes = min(min(abs(minutes_p[i]-minutes_p[i+1]), abs(1440-abs(minutes_p[i]-minutes_p[i+1]))), min_minutes)
         
         print(min_minutes)
         return min_minutes
             
         

