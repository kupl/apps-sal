def check(x,y,mat):
 tc=0
 if(mat[(x-1)][y]==0):
  tc+=1
 if(mat[(x)][y-1]==0):
  tc+=1
 if(mat[(x)][y+1]==0):
  tc+=1
 if(mat[(x+1)][y]==0):
  tc+=1
 #print(x,y,mat[x],tc)
 return tc



T=int(input())
for t in range(T):
 ls=list(map(int,input().split()))
 N=ls[0]
 M=ls[1]
 K=ls[2]
 mat=[[0 for i in range(M+2)] for i in range(N+2)]
 rows=[]
 cols=[] 
 for k in range(K):
  es=list(map(int,input().split()))
  mat[es[0]][es[1]]=1
  rows.append(es[0])
  cols.append(es[1])
 #for row in mat:
 #   print(row)
 count=0
 for i in range(len(rows)):
  count=count+check(rows[i],cols[i],mat)
 print(count)

