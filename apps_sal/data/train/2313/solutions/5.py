def f():
    return list(map(int, input().split()))


def g(j):
    return a[i] * b[j] + t[j]


def h(j, k):
    return (t[i] - t[j]) * (b[j] - b[k]) < (t[j] - t[k]) * (b[i] - b[j])


n = int(input())
(a, b) = (f(), f())
t = [0] * n
p = [0]
for i in range(1, n):
    while len(p) > 1 and g(p[1]) < g(p[0]):
        p.pop(0)
    t[i] = g(p[0])
    while len(p) > 1 and h(p[-2], p[-1]):
        p.pop()
    p.append(i)
print(t[-1])
