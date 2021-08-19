def inp():
    return int(input())


def linp():
    return list(map(int, input().split(' ')))


def minp():
    return map(int, input().split(' '))


def prn(xx):
    for yy in xx:
        print(yy, end=' ')


t = inp()
for _ in range(t):
    (n, m) = minp()
    m -= 1
    kk = m // n
    sm = n + n * kk
    sm *= kk
    sm //= 2
    print(sm)
