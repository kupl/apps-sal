import numpy as np
N = 32;

def calc(i, na, nb, isOne):
 if na < 0 or nb < 0: return 0
 if i == len(c): return not na and not nb and not isOne
 ret = dp[i][na][nb][int(isOne)]

 if ret != -1: return ret
 ret = 0

 if isOne:
  if c[i] == '0':
   ret += calc(i+1, na-1, nb, True)
   ret += calc(i+1, na, nb-1, True)
  else:
   ret += calc(i+1, na, nb, False)
   ret += calc(i+1, na-1, nb-1, True)
 else:
  if c[i] == '0':
   ret += calc(i+1, na, nb, False);
   ret += calc(i+1, na-1, nb-1, True)
  else:
   ret += calc(i+1, na-1, nb, False)
   ret += calc(i+1, na, nb-1, False)

 dp[i][na][nb][int(isOne)] = ret
 return ret


t = int(input())
dp = np.array([-1] * N * N * N * 2).reshape(N, N, N, 2)
for _ in range(t):
 a, b, c = map(int, input().split())
 c = "{0:b}".format(c)[::-1]
 x = "{0:b}".format(a).count('1')
 y = "{0:b}".format(b).count('1')
 dp.fill(-1)
 print(calc(0, x, y, False))
