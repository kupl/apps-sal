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
         if len(intervals) == 0:
             return 0
         
         intervals = sorted(intervals, key = lambda x: (x.end, -x.start))
         
         end = intervals[0].end
         
         res = 0
         
         for interval in intervals[1:]:
             
             if end > interval.start:
                 res += 1
             else:
                 end = interval.end
         
         for i in intervals:
             print((i.start,i.end))
         return res
         
         
