import sys
def input(): return sys.stdin.readline().rstrip("\r\n")


def inp(): return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


tc = 1
tc, = inp()
for _ in range(tc):
    n, = inp()
    b = (n * (n + 1)) // 2
    a = [i + 1 for i in range(b + 1)]
    start = 0
    for i in range(n, 0, -1):
        print(*a[start:start + i], sep="")
        start += i
