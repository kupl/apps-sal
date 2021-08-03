MAXN = 200100

n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
lpos = [-1] * MAXN
for i in range(n):
    lpos[a[i]] = i
need = 0
i = 0
while i < n:
    start = i
    r = lpos[a[i]]
    cnts = {}
    while i <= r:
        r = max(r, lpos[a[i]])
        if a[i] in cnts:
            cnts[a[i]] += 1
        else:
            cnts[a[i]] = 1
        i += 1
    need += i - start - max(cnts.values())

print(need)
