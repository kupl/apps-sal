from math import sqrt
def sol(p, m):
 if p == s:
  ans.append(m + N)
  return
 __pow = 1
 for i in range(ls[p][1] + 1):
  if m > N // __pow:break
  sol(p + 1, m * __pow)
  __pow *= ls[p][0]
for _ in range(int(input())):
 n = int(input())
 N, sq,ls,ans = n, int(sqrt(n)),list(),list()
 for i in range(2, sq+1):
  if n % i == 0:
   Count = 0
   while n % i == 0:
    Count += 2
    n //= i
   ls.append([i, Count])
 if n != 1:ls.append([n, 2])
 s = len(ls)
 sol(0, 1)
 ans.sort()
 print(len(ans))
 print(*ans, sep = '\n')
