import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ok = True
    for i in range(1, n):
        if p[i - 1] < p[i] and p[i - 1] + 1 != p[i]:
            ok = False
            break
    print('Yes' if ok else 'No')
