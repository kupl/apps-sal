__author__ = 'kitkat'
import sys
MAXN = int(200000.0 + 10)
try:
    while True:
        S = [0] * MAXN
        ans = [0] * MAXN
        L = [0] * MAXN
        R = [0] * MAXN
        n = int(input())
        val = list(map(int, input().split(' ')))
        top = -1
        for i in range(n):
            while ~top and val[i] <= val[S[top]]:
                top -= 1
            L[i] = S[top] if ~top else -1
            top += 1
            S[top] = i
        top = -1
        for i in range(n - 1, -1, -1):
            while ~top and val[i] <= val[S[top]]:
                top -= 1
            R[i] = S[top] if ~top else n
            top += 1
            S[top] = i
        for i in range(n):
            ans[R[i] - L[i] - 1] = max(ans[R[i] - L[i] - 1], val[i])
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i + 1])
        for i in range(1, n + 1):
            sys.stdout.write('%d ' % ans[i])
        print('')
except EOFError:
    pass
