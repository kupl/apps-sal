class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        
        if not cells:return cells
        #brute force can be optimized by finding number count aftwer which the pattern 
        #repeats. So take first day and change according to rules and update counter
        #when new updated cell matches the one u started with ,get the counter
        #this is number after which pattern repeats
        #now we can simply fast forward 
        
        day1=self.nextDay(cells)
        cells=day1.copy()
        count=0
        N-=1
        
        while N>0:
            each_day=self.nextDay(cells)
            count+=1
            N-=1
            
            if each_day==day1:
                N=N%count
            cells=each_day
        return cells
           
                
    def nextDay(self,cells):
        ret=[0]
        for i in range(1,len(cells)-1):
            ret.append(int(cells[i-1]==cells[i+1]))
        ret.append(0)
        return ret
         
            
            
        return cells
                        
            
           
    
            
#         dp=cells.copy()
#         for i in range(N):
#             for j in range(8):
#                 if j==0:
#                     if dp[j]==1:cells[j]=0
#                 elif j==7 :
#                     if dp[j]==1:cells[j]=0
#                 else:
#                     if dp[j-1]^dp[j+1]==0:
#                         cells[j]=1
#                     else:
#                         cells[j]=0
                        
                        
#             dp=cells.copy()
                
#         return cells

