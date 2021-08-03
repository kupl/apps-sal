def rd(): return list(map(int, input().split()))


def root(x):
    if f[x] != x:
        f[x] = root(f[x])
    return f[x]


n, m = rd()
N = list(range(n))
f = list(N)
lang = [0] * n
for i in N:
    lang[i] = set(rd()[1:])
for i in N:
    for j in N[:i]:
        rj = root(j)
        if lang[rj].intersection(lang[i]):
            f[rj] = i
            lang[i] = lang[i].union(lang[rj])
print(sum(1 for i in N if i == root(i)) - (sum(map(len, lang)) > 0))
