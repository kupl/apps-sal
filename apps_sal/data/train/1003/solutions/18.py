from functools import reduce


def add(x, y):
    a = n_d[y] - m_d[y]
    return a + x if a > 0 else x


a = int(input())
while(a):
    m, n = [int(x) for x in input().split(' ')]
    m_d = {}
    n_d = {}
    while(m):
        k, j = [int(x) for x in input().split(' ')]
        if(j in m_d):
            m_d[j] += k
        else:
            m_d[j] = k
        m -= 1
    while(n):
        k, j = [int(x) for x in input().split(' ')]
        if(j in n_d):
            n_d[j] += k
        else:
            n_d[j] = k
        n -= 1
    a -= 1
    print(reduce(add, iter(m_d.keys()), 0))
