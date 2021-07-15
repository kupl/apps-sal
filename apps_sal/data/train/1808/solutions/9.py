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
         intervals = sorted(intervals, key= lambda x:x.end)
         count = 1;
         last = 0;
         for i in range(1,len(intervals)):
             if intervals[last].end <= intervals[i].start:
                 count +=1
                 last = i;
         
         return len(intervals) - count
  
