def d(i, j, k):
    return sum(((a - c) * (b - c) for (a, b, c) in zip(p[i], p[j], p[k]))) * (i != j)


n = int(input())
r = range(n)
p = [list(map(int, input().split())) for i in r]
t = [k + 1 for k in r if all((d(i, j, k) <= 0 for i in r for j in r))] if n < 12 else []
print(len(t))
for q in t:
    print(q)
