k,n = map(int,input().split())
if k%2 == 0:
  ans = [k//2]+[k]*(n-1)
else:
  t = n//2
  ans = [k//2+1]*n
  for i in range(t):
    if ans[-1] == 1:
      ans.pop()
    else:
      ans[-1] -= 1
      while len(ans) < n:
        ans.append(k)
print(*ans)
