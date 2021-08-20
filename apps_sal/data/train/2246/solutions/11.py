def R():
    return map(int, input().split())


(n, k) = R()
xs = list(R())
a = int(input())
cs = list(R())
r = j = 0
try:
    for (i, x) in enumerate(xs):
        while x > k:
            s = min(cs[:i + 1 - j])
            cs.remove(s)
            j += 1
            k += a
            r += s
except:
    print(-1)
    quit()
print(r)
