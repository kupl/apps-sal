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
         intervals.sort(key=lambda x: (x.start, x.end))
         
         num_removed = 0
         current_interval_end = float('-inf')      
         for interval in intervals:
             if interval.start >= current_interval_end:
                 # No overlap
                 current_interval_end = interval.end
             else:
                 # Overlapping intervals. Remove interval with latest end time
                 current_interval_end = min(current_interval_end, interval.end)
                 num_removed += 1
         return num_removed
