from functools import reduce
def add(x, y):
    a = n_d[y] - m_d[y]
    return a+x if a>0 else x

a = int(input())
for u in range(a):
    m, n = list(map(int, input().split()))
    m_d = {}
    n_d = {}
    for v in range(m):
        k, j = list(map(int, input().split()))
        if(j in m_d):
            m_d[j] += k
        else:m_d[j] = k
    for w in range(n):
        k, j = list(map(int, input().split()))
        if(j in n_d):
            n_d[j] += k
        else:n_d[j] = k
    print(reduce(add, iter(m_d.keys()), 0))


