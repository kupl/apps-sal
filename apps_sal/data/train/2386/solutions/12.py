t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  ans=[]
  visited=set()
  for i in range(2*n):
    if not a[i] in visited:
      ans.append(str(a[i]))
      visited.add(a[i])
  print(' '.join(ans))
