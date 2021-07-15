
import sys
try:
    while True:
        n = int(input())
        height = list(map(int, input().split(" ")))
        L = [0 for i in range(100001)]
        R = [0 for i in range(100001)]
        for i in range(n):
            L[i+1] = min(L[i]+1, height[i])
        for i in range(n-1, -1, -1):
            R[i] = min(R[i+1]+1, height[i])
        ans = 0
        for i in range(1, n+1):
            ans = max(ans, min(R[i-1], L[i]))
        print(ans)
except EOFError:
    pass
