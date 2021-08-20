n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))
ans = sum((q != w for (q, w) in zip(a, b)))
i = 1
while i < n:
    aii = a[i - 1]
    ai = a[i]
    bii = b[i - 1]
    bi = b[i]
    if aii + ai == 1 and bii + bi == 1 and (aii != bii) and (ai != bi):
        ans -= 1
        i += 1
    i += 1
print(ans)
