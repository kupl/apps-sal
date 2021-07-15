from math import sqrt
for _ in range(int(input())):
 n = int(input())
 r = int(sqrt(n))
 print("YES" if r * r == n else "NO")
