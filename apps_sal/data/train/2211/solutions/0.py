import sys
input = sys.stdin.readline


def mii():
    return list(map(int, input().split()))


for _ in range(int(input())):
    (n, x) = mii()
    has = 0
    a = 0
    for i in mii():
        if x == i:
            has = 1
        a = max(a, i)
    if has:
        print(1)
    else:
        print(max(2, (x - 1) // a + 1))
