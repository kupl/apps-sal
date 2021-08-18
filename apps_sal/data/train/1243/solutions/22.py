import sys
def input(): return sys.stdin.readline().rstrip("\r\n")


def inp(): return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


tc = 1
tc, = inp()
for _ in range(tc):
    n, = inp()
    print(1 if any([int(i) % 5 == 0 for i in str(n)]) else 0)
