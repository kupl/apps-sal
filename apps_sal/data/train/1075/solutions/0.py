gb = [0, 1, 2, 2, 3, 3]
ga = [0 for x in range(70)]
gag = [0 for x in range(70)]
ga[0] = 1
gag[0] = 0

for i in range(1, 70):
 if i % 4 == 0:
  ga[i] = 1.5 * ga[i-1]
  gag[i] = 0
 else:
  ga[i] = 2 * ga[i-1]
  gag[i] = gag[i-1] + 1


def g(n):
 if n < 6:
  return gb[n]
 else:
  x = n / 6
  a = 0
  for i, k in enumerate(ga):
   if k <= x:
    a = i
   else:
    break
  return gag[a]


t = int(input())
for q in range(t):
 n = int(input())
 a = list(map(int, input().split()))

 res = g(a[0])
 for i in range(1, n):
  res ^= g(a[i])

 if res == 0:
  print("Derek")
 else:
  print("Henry")

