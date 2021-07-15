t=int(input())
while t:
  n,k=input().split(" ")
  n=int(n)
  k=int(k)
  ans=2*(n-((n-1)/k))
  print(ans)
  t-=1
