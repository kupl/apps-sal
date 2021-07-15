n, r = [int(x) for x in input().split()]

n = 2 ** n

xs = [int(x) for x in input().split()]

s = sum(xs)

res = [0 for _ in range(r+1)]
for i in range(r):
    res[i] = s / n
    i, val = [int(x) for x in input().split()]
    s += val - xs[i]
    xs[i] = val
res[r] = s / n
print("\n".join(map(str, res)))

