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
         start_end={}
         for i in intervals:
             if i.start in start_end:
                 if start_end[i.start]>i.end:
                     start_end[i.start]=i.end
             else:
                 start_end[i.start]=i.end
         final_list={}
         if len(start_end)>1:
             sorted_list=sorted(start_end)
 
             for i,j in enumerate(sorted_list):
                 if i>0:
                     start2=j
                     #if j>-90 and j<-80:
                     #    print(start1,end1,start2,start_end[start2])
                     if start2<end1:
                         if start_end[start2]<end1:
                             final_list.pop(start1,None)
                             end2=start_end[start2]
                             final_list[start2]=end2
                             end1=end2
                             start1=start2
                             #if j>-90 and j<-80:
                             #    print(start1,end1)
                         elif end1<=start_end[start2]:
                             final_list[start1]=end1
                             end1=end1
                             start1=start1
                             #if j>-90 and j<-80:
                             #    print(start1,end1)
                     elif start2>=end1:
                         final_list[start1]=end1
                         start1=start2
                         end1=start_end[start2]
                         if i==len(sorted_list)-1:
                             final_list[start2]=start_end[start2]
                 if i==0:
                     start1=j
                     end1 =start_end[j]
         elif len(start_end)==1:
             final_list=start_end
         print(list((i,start_end[i]) for i in sorted(start_end)))
         print('result') 
         print(list((i,final_list[i]) for i in sorted(final_list)))
         return len(intervals)-len(final_list)
                 
                 
                 
