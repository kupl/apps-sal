import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1, 0, -1):
        a[i] -= a[i - 1]
    minus = 0
    for i in range(1, n):
        if a[i] < 0:
            minus -= a[i]
    if a[0] - minus >= 0:
        print('YES')
    else:
        print('NO')
