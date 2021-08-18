n = int(input())
w = []
h = []
c = []
cntw = {}
cnth = {}
multMayotC = 0
cntC = 0


def insert1(a, b, c):
    if not a in b:
        b[a] = c
    else:
        b[a] = b[a] + c


def multMayot(a, b):
    if a % b == 0:
        return b
    else:
        return multMayot(b, a % b)


for i in range(0, n):
    a, b, d = map(int, input().split())
    w.append(a)
    h.append(b)
    c.append(d)
    insert1(a, cntw, d)
    insert1(b, cnth, d)
    cntC += d

    if multMayotC == 0:
        multMayotC = d
    else:
        multMayotC = multMayot(multMayotC, d)

for i in range(0, n):
    if cntw[w[i]] * cnth[h[i]] != cntC * c[i]:
        print(0)
        return

result = 0
i = 1
while (i * i <= multMayotC):
    if multMayotC % i == 0:
        result += 1
        if i * i != multMayotC:
            result += 1
    i += 1

print(result)
