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
         s_intervals = [(intervals[i].start, intervals[i].end) for i in range(len(intervals))]
         s_intervals.sort()
         s_intervals = [(s_intervals[i][0], s_intervals[i][1], i) for i in range(len(intervals))]
         f_intervals = [(j,i,h) for (i,j,h) in s_intervals]
         f_intervals.sort()
         f_intervals = [(j,i,h) for (i,j,h) in f_intervals]
         
         skipped = 0
         bound = 0
         for interval in f_intervals:
             if interval[2] < bound:
                 continue
             i = bound
             for i in range(bound, len(intervals)):
                 if s_intervals[i][2] == interval[2]:
                     continue
                 if s_intervals[i][0] >= interval[1]:
                     break
                 else:
                     skipped += 1
             bound = i
         return skipped
                 
