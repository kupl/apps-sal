# cook your dish here
n,m=map(int,input().split())
for _ in range(m):
  q=int(input())
  if q<n+2 or q>2*n+n:
    print(0)
    continue
  else:
    low=n+2
    high=2*n+n
    count=1+min(abs(q-low),abs(q-high))
    print(count)  


