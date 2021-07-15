t=int(input())
for i in range(t):
 n=int(input())
 l=list(map(int,input().split()))
 l.sort()
 s=0
 for k in range(n//2):
  s+=abs(l[n-k-1]-l[k])
 print(s)
