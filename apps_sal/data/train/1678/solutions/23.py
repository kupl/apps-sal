from itertools import *
def f(): return map(int, input().split())


a, b = f()
l = list(f())
m = list(f())
m_a = l.index(min(l))
m_b = m.index(max(m))
for i in range(b):
    print(m_a, i)
for i in range(a):
    if i != m_a:
        print(i, m_b)
