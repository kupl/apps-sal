import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cum = [0 for _ in range(2 * k + 2)]
    for i in range(n // 2):
        x, y = a[i], a[n - i - 1]
        cum[2] += 2
        cum[min(x, y) + 1] -= 1
        cum[x + y] -= 1
        cum[x + y + 1] += 1
        cum[max(x, y) + k + 1] += 1
        cum[2 * k + 1] -= 2
    ans = n
    for i in range(2, 2 * k + 1):
        cum[i] += cum[i - 1]
        ans = min(ans, cum[i])
    print(ans)
