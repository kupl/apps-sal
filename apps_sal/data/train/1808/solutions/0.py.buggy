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
         intervals = sorted(intervals, key = lambda x: x.end)
         current_end = float('-inf')
         cnt = 0
         for interval in intervals:
             if interval.start >= current_end:
                 cnt += 1
                 current_end = interval.end
         return len(intervals) - cnt
         
