n,k = map(int,input().split())
ar = sorted(list(map(int,input().split())))
cnt = 0
_sum = 0
for i in ar:
 if i+_sum <= k:
  cnt+=1
  _sum+=i
 else:
  break
print(cnt)
