# cook your dish here
t=int(input())
while(t!=0):
 t-=1
 n=int(input())
 fg=list(map(int,input().split()))
 for i in range(1,n):
  fg[i]=min((fg[i-1]+1),fg[i])
 for j in range(n-2,-1,-1):
  fg[j]=min((fg[j+1]+1),fg[j])
 print(*fg)

