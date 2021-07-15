# Definition for an interval.
 # class Interval:
 #     def __init__(self, s=0, e=0):
 #         self.start = s
 #         self.end = e
 
 class Solution:
     def eraseOverlapIntervals(self, intervals):
         """
         :type intervals: List[Interval]
         :rtype: int
         """
         if not intervals:
             return 0
         intervals.sort(key=lambda x:x.start) # start or end doesn't matter
         latest = intervals[0].end # always check end 
         count = 0
         for interval in intervals[1:]:
             if interval.start < latest:
                 count += 1
                 latest = min(latest, interval.end)
             else:
                 latest = interval.end
         return count
