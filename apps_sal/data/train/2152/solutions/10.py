n = int(input())
a = list(map(int,input().split()))
if sum(a) == 1:
  print(-1)
  return
sm = sum(a)
nmax = 10**5+10
eratos = [0 for i in range(nmax+1)]
prime = []
cnt = 2
while True:
  while cnt <= nmax and eratos[cnt]:
    cnt += 1
  if cnt > nmax:
    break
  eratos[cnt] = 1
  prime.append(cnt)
  for i in range(cnt**2,nmax+1,cnt):
    eratos[i] = 1
dvls = []
for i in prime:
  if sm%i == 0:
    dvls.append(i)
ansls = []
ls = []
cnti = 0
for dv in dvls:
  ans = 0
  if dv == 2:
    for i in range(n):
      if a[i]:
        cnti += 1
        if cnti%2:
          pivot = i
        else:
          ans += i-pivot
  else:
    for i in range(n):
      if a[i]:
        cnti += 1
        if 1 <= cnti%dv <= dv//2:
          ls.append(i)
        elif cnti%dv == dv//2+1:
          pivot = i
          for j in ls:
            ans += pivot-j
          ls.clear()
        else:
          ans += i-pivot
  ansls.append(ans)
print(min(ansls))
