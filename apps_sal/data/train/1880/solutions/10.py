from queue import deque
from collections import defaultdict
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        def next_day(c)->List[int]:
            res=[0]*8
            for i in range(1,7):
                if c[i-1]==c[i+1]:res[i]=1
                else:res[i]=0
            return res
        
        def period(c)->int:
            if c[0]!=0 or c[-1]!=0: return 0
            temp=c
            for day in range(1,2**6+1):
                if day==2**6: return 0
                temp=next_day(temp)
                if temp==c:return day
        
                
        temp=cells
        
        for day in range(1,N+1):
            temp=next_day(temp)
            if period(temp):break
        
        N=(N-day)%period(temp)
        for day in range(1,N+1):
            temp=next_day(temp)
        
        
        
        return temp
