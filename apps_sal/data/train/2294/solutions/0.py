import sys


def input():
    return sys.stdin.readline()[:-1]


n = int(input())
d = []
M, m = 0, 10**30
M_of_m, m_of_M = 0, 10**30
for _ in range(n):
    x, y = map(int, input().split())
    g, l = max(x, y), min(x, y)
    d.append([l, g])
    M = max(M, g)
    m = min(m, l)
    M_of_m = max(M_of_m, l)
    m_of_M = min(m_of_M, g)
ans1 = (M - m_of_M) * (M_of_m - m)

M_other, m_other = M_of_m, m
m_reversed = 10**30
gap = M_other - m_other
d.sort(key=min)
for i in range(n - 1):
    M_other = max(M_other, d[i][1])
    m_reversed = min(m_reversed, d[i][1])
    m_other = min(m_reversed, d[i + 1][0])
    gap = min(gap, M_other - m_other)
M_other = max(M_other, d[n - 1][1])
m_reversed = min(m_reversed, d[i][1])
gap = min(gap, M_other - m_reversed)
ans2 = (M - m) * gap

print(min(ans1, ans2))
