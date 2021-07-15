# 17:06
 class Solution:
     def findMinDifference(self, timePoints):
         """
         :type timePoints: List[str]
         :rtype: int
         """
 
         t = [int(y[0])*60 + int(y[1]) for x in timePoints for y in [x.split(":")]]   ## HH * 60 + MM
         t = sorted(t)
 
         t.append(t[0]+24*60)
         print(t)
         best = float("inf")
         for i in range(len(timePoints)):
             best = min(best, (t[i+1]-t[i]))
         return best
 # 17:10
 # 17:16 be careful of line 9: ... for y in [ ... ]; otherwise we will be looking at one number at a time
 # 17:18 should not do MOD 12 hours
              
