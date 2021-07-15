k,n = map(int,input().split())
if k %2 ==0:
  ans = []
  ans.append(k//2)
  for i in range(n-1):
    ans.append(k)
  print(*ans)
else:
  ans = []
  for i in range(n):
    ans.append(k//2+1)
  sage = (n)//2
  for i in range(sage):
    if ans[-1] == 1:
      ans.pop()
    else:
      ans[-1] -= 1
      while len(ans) < n:
        ans.append(k)
  print(*ans)
