from math import pi
for _ in range(int(input())):
  r1, h1, r2, h2 = list(map(float, input().split()))
  print("%0.6f %0.6f"%(r1 ** 2 * pi * h1 / 3 + r1 ** 3 * pi * 2 / 3, r2 ** 2 * pi * h2))

