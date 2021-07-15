t=int(input())
for i in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort()
 m=a[0]
 ans=(len(a)-1)*m
 print(ans)

