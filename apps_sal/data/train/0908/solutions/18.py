import math
t = int(input())
for i in range(t):
    n = int(input())
    ans = math.sqrt(8 * n + 1) + 1
    print(int(ans / 2 - 1))
