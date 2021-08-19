def I():
    return map(int, input().split())


(n, k) = I()
r = k - 1
y = 0
for _ in range(k):
    t = list(I())
    for i in range(1, t[0]):
        if t[i] == y + 1:
            y += 1
            if t[i + 1] != t[i] + 1:
                r += 2
        else:
            if y:
                y = -1
            r += 2
print(r)
