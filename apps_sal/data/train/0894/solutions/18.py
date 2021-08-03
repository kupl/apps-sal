t = int(input())
a = []
while t > 0:
    a = []
    b = []
    n = int(input())
    for i in range(n):
        k = list(map(int, input().split()))
        z = 0
        for j in k:
            z = 2 * z + j
        a.append(z)
    for i in range(n):
        k = list(map(int, input().split()))
        z = 0
        for j in k:
            z = 2 * z + j
        b.append(z)
    aindex = list(range(n))
    bindex = list(range(n))
    c = aindex
    for i in range(n):
        c[i] = 0

    for i in range(n):
        max = -1
        maxindex = 0
        for j in range(n):
            temp = ~(a[i] ^ b[j])
            if temp > max and c[j] == 0:
                max = temp
                maxindex = j
        bindex[maxindex] = i + 1
        c[maxindex] = 1
    for i in range(n):
        print(i + 1, end=' ')
    print()
    for j in bindex:
        print(j, end=' ')
    print()
    t = t - 1
