t=int(input())
for T in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 l.sort()
 res=l[0]
 for i in range(1,n):
  res=res%l[i]
 print(res)

