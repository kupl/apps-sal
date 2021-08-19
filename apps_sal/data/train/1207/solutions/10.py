# cook your dish here
t = int(input())


def kingship(p, n):

    s = 0
    m = min(p)

    for i in range(0, n):
        s += p[i] * m
    return s - m * m


for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    r = kingship(p, n)
    print(r)
