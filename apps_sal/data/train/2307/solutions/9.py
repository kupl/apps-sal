import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))


def write(x):
    return sys.stdout.write(x + '\n')


(n, a, b) = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 0
for i in range(n - 1):
    if (x[i + 1] - x[i]) * a > b:
        ans += b
    else:
        ans += (x[i + 1] - x[i]) * a
print(ans)
