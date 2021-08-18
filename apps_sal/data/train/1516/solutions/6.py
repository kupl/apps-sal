import math
t = int(input())
for _ in range(t):
    m = 10**9 + 7
    n, k = list(map(int, input().split()))
    if(n == 2):
        print(((k * (k - 1)) // 2) % m)
