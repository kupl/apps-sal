import sys
def input(): return sys.stdin.readline().rstrip("\r\n")


def inp(): return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


tc = 1
tc, = inp()
for _ in range(tc):
    n, = inp()
    if n == 1:
        print(1)
        continue
    c = 1
    print(1)
    c += 1
    for i in range(n - 2):
        print(str(c) + ' ' * (i) + str(c + 1))
        c += 2
    print(*[c + i for i in range(n)], sep="")
