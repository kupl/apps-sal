# cook your dish here
def checkStability(inp_arr,R,C,i,j):
 cell_cnt=0
 for coordinates in ((i,j-1),(i,j+1),(i-1,j),(i+1,j)):
  r,c=coordinates
  if(r>=0
  and c>=0
  and r<R
  and c<C):
   cell_cnt+=1
  
 if(inp_arr[i][j]>=cell_cnt):
  return False
 return True
 
for _ in range(int(input())):
 R,C=(int(i) for i in input().strip(' ').split(' '))
 inp_arr=[]
 stableFlag=True
 printStr='Stable'
 for i in range(R):
  inp_arr.append(tuple(int(i) for i in input().strip(' ').split(' ')))
 for i in range(R):
  if(stableFlag==True):
   for j in range(C):
    stableFlag=checkStability(inp_arr,R,C,i,j)
    if(stableFlag==False):
     printStr='Unstable'
     break
 print(printStr)

