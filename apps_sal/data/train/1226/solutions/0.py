from collections import defaultdict
from itertools import product

def solve(mouse,n,m):
 
 # shadow matrix will contains the count of mice which affect (i,j) position
 # if there is a mice at position (i,j) then in shadow matrix it will affect         all four adjacent blocks 
 shadow=[[0 for i in range(m)]for j in range(n)]
 for i,j in product(list(range(n)),list(range(m))):
  if mouse[i][j]==1:
   if i>0:
    shadow[i-1][j]+=1
   if j>0:
    shadow[i][j-1]+=1
   if i<n-1:
    shadow[i+1][j]+=1
   if j<m-1:
    shadow[i][j+1]+=1
 
 # dp is a dictionary which contains a tuple of 3 values (i,j,0)=>we are         coming at destination (i,j) from left side
 # (i,j,1)=> we are coming at destination (i,j) from top 
 dp=defaultdict(int)
 
 # 
 dp[(0,0,0)]=dp[(0,0,1)]=shadow[0][0]-mouse[0][0]
 
 # fill only first row
 # in first row we can only reach at (0,j) from (0,j-1,0) as we can't come         from top.
 
 # so here we will assign count of mices which will affect current cell        (shadow[0][i]) + previous result i.e,(0,j-1,0) and 
 # if mouse is in the current cell than we have to subtract it bcoz we have         add it twice i.e, when we enter at this block 
 # and when we leave this block 
 for i in range(1,m):
  dp[(0,i,0)]=dp[(0,i,1)]=shadow[0][i]-mouse[0][i]+dp[(0,i-1,0)]
 
 # same goes for first column
 # we can only come at (i,0) from (i-1,0) i.e top
 for i in range(1,n):
  dp[(i,0,0)]=dp[(i,0,1)]=shadow[i][0]-mouse[i][0]+dp[(i-1,0,1)]
 
 
 # for rest of the blocks 
 # for a block (i,j) we have to add shadow[i][j] and subtract mouse[i][j]         from it for double counting
 # now for each block we have two choices, either take its previous block         with same direction or take previous block with different 
 # direction and subtract corner double counted mouse. We have to take min of         both to find optimal answer
 for i,j in product(list(range(1,n)),list(range(1,m))):
  a=shadow[i][j]-mouse[i][j]
  b=a
  a+=min(dp[(i,j-1,0)],dp[(i,j-1,1)]-mouse[i-1][j])
  b+=min(dp[(i-1,j,1)],dp[(i-1,j,0)]-mouse[i][j-1])
  dp[(i,j,0)]=a
  dp[(i,j,1)]=b
  
 # what if [0][0] and [n-1][m-1] have mice, so we have to add them as we         haven't counted them yet.
 
 return min(dp[(n-1,m-1,0)],dp[(n-1,m-1,1)])+mouse[0][0]+mouse[n-1][m-1]
    
for _ in range(int(input())):
 n,m=list(map(int,input().split( )))
 mouse=[]
 for i in range(n):
  x=input()
  mouse.append(list(map(int,x)))
 print(solve(mouse,n,m))
 
    
    
    
    
    
    
    
    
    

