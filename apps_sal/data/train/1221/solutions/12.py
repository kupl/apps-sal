import sys
import math
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = 0
    y = 0
    ans = 0
    while x <= n:
        z = int(math.sqrt(y))
        z += 1
        y += z * z
        x = z
        ans += 1
    print(ans - 1)
