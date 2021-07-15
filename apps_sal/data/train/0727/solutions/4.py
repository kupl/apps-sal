import sys
first = True
memmin = {}
memmax = {}

def fmax(n):
 if n == 1: return 2
 if n == 0: return 0
 if n in memmax: return memmax[n]

 res = 0
 for i in range(n):
  cur = i + 1 + n - i + fmax(i) + fmax(n-i-1)
  if cur > res: res = cur

 memmax[n] = res
 return res

def fmin(n):
 if n == 1: return 2
 if n == 0: return 0
 if n in memmin: return memmin[n]

 res = 10 ** 9
 for i in range(n):
  cur = i + 1 + n - i + fmin(i) + fmin(n-i-1)
  if cur < res: res = cur

 memmin[n] = res
 return res 

for line in sys.stdin:
 if first:
  first = False
  tc = int(line)
  continue

 tc -= 1
 if tc < 0: break

 n, m = list(map(int, line.split()))

 val1 = fmin(n)
 val2 = fmax(n)

 if m < val1: print(-1)
 else:
  if m > val2: print(m - val2)
  else: print(0)
