from bisect import bisect_left
m = int(input())
t, s = [input().split() for i in range(m)], [0] * m
l, n = 0, int(input())
for j, i in enumerate(t):
    l += 1 if i[0] == '1' else int(i[1]) * int(i[2])
    t[j], s[j] = l, i[1] if i[0] == '1' else int(i[1])
F = {}


def f(i):
    if not i in F:
        k = bisect_left(t, i)
        F[i] = s[k] if type(s[k]) == str else f((i - t[k] - 1) % s[k] + 1)
    return F[i]


print(' '.join(f(i) for i in map(int, input().split())))
