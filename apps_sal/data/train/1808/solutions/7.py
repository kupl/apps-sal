# Definition for an interval.
 # class Interval:
 #     def __init__(self, s=0, e=0):
 #         self.start = s
 #         self.end = e
 
 class Solution:
     def eraseOverlapIntervals(self, intervals):
         if not intervals: return 0
         intervals = sorted(intervals, key=lambda x: x.end)
         prev_end = intervals[0].end
         count = 0
         for i in intervals[1:]:
             if i.start < prev_end:
                 count += 1
             else:
                 prev_end = i.end
         return count
