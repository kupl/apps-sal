# cook your dish here
t=int(input())
for j in range(0,t):
 n,k=list(map(int,input().split()))
 summ=0
 maxm=n-k+1
 if(k>n):
  summ=0
 else:
  for i in range(1,n+1):
   summ+=i
   if(i==maxm):
    break
 print('Case '+str(j+1)+':',summ)

