N, = list(map(int, input().split()))
X = list(map(int, input().split()))

sx = []
c = 0
d = dict()
for x in sorted(list(set(X))):
    sx.append(x)
    d[x] = c
    c += 1
sx.append(10**18)

count = [0] * (c + 1)
for x in X:
    count[d[x]] += 1
for i in range(c - 1, -1, -1):
    count[i] += count[i + 1]

count2 = [0] * (c + 1)
for i in range(c - 1, -1, -1):
    count2[i] = count[i + 1] * (sx[i + 1] - sx[i])
for i in range(c - 1, -1, -1):
    count2[i] += count2[i + 1]


Y = []
for i in range(N):
    Y.append((X[i], -i))
Y.sort()
R = []
while Y:
    y, j = Y.pop()
    j = -j
    if not R:
        R.append((d[y], j))
    else:
        if d[y] < R[-1][0] and j < R[-1][1]:
            R.append((d[y], j))


RR = [0] * N
b = 0
bi = 0
for y, i in R[:]:
    RR[bi] = count2[y] - b
    b = count2[y]
    bi = i
RR[0] = sum(X) - sum(RR[1:])
for r in RR:
    print(r)
