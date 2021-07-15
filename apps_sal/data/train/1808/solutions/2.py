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
         if len(intervals) <= 1: return 0
         min_removals = 0
         j = 1
         intervals = sorted(intervals, key=lambda i: (i.start, i.end))
         endpoint = intervals[0].end
         
         while j < len(intervals):
             if intervals[j].start < endpoint:
                 min_removals+=1
                 endpoint = min(endpoint, intervals[j].end)
             else:
                 endpoint = intervals[j].end
             j+=1
         
         return min_removals
         
         
             
