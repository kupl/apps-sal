def f(x, ud, li):
    if not ud:
        return 1
    m = 1
    if x + 1 in ud:
        ud1 = ud[:]
        ud.remove(x + 1)
        m += f(x + 1, ud, li)
        ud = ud1[:]
    if x - 1 in ud:
        ud1 = ud[:]
        ud.remove(x - 1)
        m += f(x - 1, ud, li)
        ud = ud1[:]
    if li[x] == 2:
        if x + 2 in ud:
            ud1 = ud[:]
            ud.remove(x + 2)
            m += f(x + 2, ud, li)
            ud = ud1[:]
        if x - 2 in ud:
            ud1 = ud[:]
            ud.remove(x - 2)
            m += f(x - 2, ud, li)
            ud = ud1[:]
    return m


for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ud = []
    for i in range(1, n):
        ud.append(i)
    c = f(0, ud, a)
    x = 7 + pow(10, 9)
    print(c % x)
