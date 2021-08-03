def check(a, b, c):
    s = 0
    for i in range(5):
        s += (b[i] - a[i]) * (c[i] - a[i])
    return s <= 0


n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

if n == 1 or n == 2:
    print(n)
    print(1)
    if n == 2:
        print(2)
    return

v = -1
i = 0
while i + 1 < n:
    if v == -1:
        if i + 2 < n:
            if check(a[i], a[i + 1], a[i + 2]):
                v = i
            elif check(a[i + 1], a[i], a[i + 2]):
                v = i + 1
            elif check(a[i + 2], a[i], a[i + 1]):
                v = i + 2
        else:
            break
    else:
        if not check(a[v], a[i], a[i + 1]):
            if check(a[i], a[v], a[i + 1]):
                v = i
            elif check(a[i + 1], a[v], a[i]):
                v = i + 1
            else:
                v = -1
    i += 1

if v == -1:
    print(0)
    return

for i in range(n):
    if i == v:
        continue
    for j in range(i + 1, n):
        if j == v:
            continue
        if not check(a[v], a[i], a[j]):
            print(0)
            return

print(1)
print(v + 1)
return
