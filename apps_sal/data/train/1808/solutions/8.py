class Solution:
     def eraseOverlapIntervals(self, intervals):
         intervals.sort(key=lambda x:x.end)        
         end = -sys.maxsize
         count = 0
         for i in intervals:
             if i.start<end: continue
             end = i.end
             count += 1
         return len(intervals)-count
