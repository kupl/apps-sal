
p, s = list(map(int, input().split()))

nvalues = []

for i in range(p):

    difficult = [0, 0]

    n = 0

    sc = list(map(int, input().split()))

    ns = list(map(int, input().split()))

    a = list(zip(sc, ns))

    a.sort()

    for j in range(s - 1):

        if(a[j][1] > a[j + 1][1]):

            n = n + 1

    difficult[0] = n

    difficult[1] = i

    nvalues.append(difficult)

nvalues.sort(key=lambda x: x[0])

for j in range(p):

    print(nvalues[j][1] + 1)
