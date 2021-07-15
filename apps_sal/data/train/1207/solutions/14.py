t=int(input())
for i in range(t):
 n=int(input())
 a=list(map(int, input().split()))
 a.sort()
 s=0
 for j in range(1,n):
  s+=a[j]*a[0]
 print(s)

