N, = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = []
for i in range(N):
    Y.append((X[i], -i))

sx = []
c = 0
d = dict()
for x in sorted(list(set(X))):
    sx.append(x)
    d[x] = c
    c += 1
sx.append(10**18)

count = [0]*(c+1)
for x in X:
    count[d[x]] += 1
for i in range(c-1, -1, -1):
    count[i] += count[i+1]

count2 = [0]*(c+1)
for i in range(c-1, -1, -1):
    count2[i] = count[i+1]*(sx[i+1]-sx[i])
for i in range(c-1, -1, -1):
    count2[i] += count2[i+1]



Y.sort()
R = []
while Y:
    y, j = Y.pop()
    if not R:
        R.append((y, -j))
    else:
#        print(y, j, R[-1])
        if y < R[-1][0] and -j < R[-1][1]:
            R.append((y, -j))



#print(count2)
#print(R)
RR = [0]*N
b = 0
bi = 0
for y, i in R[:]:
#    print(y, d[y], i, bi)
#    print(i, bi, count2[d[y]])

    RR[bi] = count2[d[y]]-b
    b = count2[d[y]]
    bi = i
RR[0] = sum(X)-sum(RR[1:])
for r in RR:
    print(r)

