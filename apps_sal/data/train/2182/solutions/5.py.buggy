a = list(input())
b = list(input())
n = len(a)
if len(a) == 1:
    print(a[0])
    return
a.sort()
b.sort()
a = a[:(len(a) + 1) // 2]
if n % 2 == 1:
    b = b[(len(b) // 2) + 1:]
else:
    b = b[(len(b) // 2):]
sa = 0
ea = len(a) - 1
sb = 0
eb = len(b) - 1
stb = 0
ste = n - 1
st = [""] * n

for i in range(n):
    if i % 2 == 0:
        if a[sa] < b[eb]:
            st[stb] = a[sa]
            sa += 1
            stb += 1
        else:
            st[ste] = a[ea]
            ea -= 1
            ste -= 1
    else:
        if eb == sb and n % 2 == 0:
            st[stb] = b[eb]
            break
        if b[eb] > a[sa]:
            st[stb] = b[eb]
            eb -= 1
            stb += 1
        else:
            st[ste] = b[sb]
            ste -= 1
            sb += 1
for i in range(len(st)):
    print(st[i], end="")
