f = 5003*[0]
modn = 1000000007


def qPow(a, b):
 nonlocal modn
 res = 1
 while b > 0:
  if (b & 1) == 1:
   res = res * a % modn
  a = a * a % modn
  b = b >> 1
 return res


def getF():
 nonlocal f
 f[0] = 1
 for i in range(1, 5001):
  f[i] = f[i-1] * i


def __starting_point():
 getF()
 T = int(input())
 while T > 0:
  T = T - 1
  n, k = list(map(int,input().split()))
  lis = list(map(int, input().split()))
  lis = sorted(lis)
  res = 1
  for i in range(n):
   zhi = f[n-1]//f[k-1]//f[n-k]
   if i >= k-1:
    zhi = zhi - f[i]//f[k-1]//f[i+1-k]
   if n-i-1 >= k-1:
    zhi = zhi - f[n-i-1]//f[k-1]//f[n-i-k]
   zhi = zhi % (modn-1)
   # print(zhi)
   res = res * qPow(lis[i], zhi) % modn
  print(res)

__starting_point()
