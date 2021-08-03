import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    used = [False for _ in range(n)]
    for i in range(n):
        if used[(i + a[i]) % n]:
            print("NO")
            break
        else:
            used[(i + a[i]) % n] = True
    else:
        print("YES")
