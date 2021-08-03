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
    j = i + 1
    while j < r:
        r = max(r, lpos[a[j]])
        j += 1
    cnts = {}
    while i <= r:
        if a[i] in cnts:
            cnts[a[i]] += 1
        else:
            cnts[a[i]] = 1
        i += 1
    best = 0
    for k, v in list(cnts.items()):
        best = max(best, v)
    need += i - start - best

print(need)
