import math
t, x = list(map(float, input().split()))
for _ in range(int(t)):
    n = int(input())
    if n < 0:
        n = -1 * n
    s = int(math.sqrt(n))
    diff = n - (s * s)
    if diff <= ((x * n) / 100):
        print("yes")
    else:
        print("no")
