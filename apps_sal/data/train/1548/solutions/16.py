t=int(input())
for _ in range(t):
 n=int(input())
 ls=list(map(int,input().split()))
 ldp=ls.copy()
 counter=-1
 for i in ldp:
  counter+=1
  if counter==0:
   continue
  ldp[counter]=min(ldp[counter],ldp[counter-1]+1)
 # print(ldp)
 rdp=ldp.copy()
 for j in range(1,n):
  rdp[n-j-1]=min(rdp[n-j-1],rdp[n-j]+1)
 print(*rdp)

