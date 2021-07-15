for _ in range(int(input())):
 n,m=map(int,input().split())
 drinks=list(map(int,input().split()))
 output=0
 remain=[]
 olist=[0]*n 
 for i in range(n):
  demand,goodp,badp=map(int,input().split())
  if drinks[demand-1]!=0:
   drinks[demand-1]-= 1 
   olist[i]=demand 
   output+=goodp 
  else:
   remain.append(i)
   output+=badp 
 rj=0
 for i in range(len(drinks)):
  if drinks[i]==0:
   continue
  while(drinks[i]>0):
   if rj==len(remain):
    break
   olist[remain[rj]]=i+1
   rj+=1 
   drinks[i]-=1
  if rj==len(remain):
   break
 
 print(output)
 for i in olist:
  print(i,end=" ")
 print()
