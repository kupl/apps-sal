from sys import stdin
input = stdin.readline


def R():
    return map(int, input().split())


def I():
    return int(input())


n = I()
v = [1] * n
a = list(R())
d = {}
for (i, j) in enumerate(sorted(a)):
    d[j] = i
for i in range(n):
    a[i] = d[a[i]]
ans = []
for i in a:
    if v[i]:
        ans += ([],)
        while v[i]:
            ans[-1] += (i + 1,)
            v[i] = 0
            i = a[i]
print(len(ans))
for i in ans:
    print(len(i), *i)
