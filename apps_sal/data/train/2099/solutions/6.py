r = list(map(int, input().split()))
n = r[0]
k = r[1]
l = list()
l.append(1)
c = k
justI = 0
maxl = 0
previous = 1
print(1, end=' ')
for i in range(1, n):
    if justI == 1:
        print(maxl + 1, end=' ')
        maxl += 1
    else:
        print(previous + c, end=' ')
        previous = previous + c
        if previous > maxl:
            maxl = previous
        if c > 1:
            c -= 1
            c *= -1
        elif c < -1:
            c += 1
            c *= -1
        else:
            justI = 1
