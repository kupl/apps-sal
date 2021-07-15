import sys

n = int(sys.stdin.readline())

for _ in range(n):
 p1, p2, m = list(map(int, sys.stdin.readline().split()))

 l = min(p1, p2)

 #while(m > 0 and l > 0):
 #    k = min(l, m)
 #    l -= k
 #    m -= 1

 q = min(p1, p2)
 d = min((m * (m + 1)) / 2, q)

 print(p1 - d + p2 - d)
