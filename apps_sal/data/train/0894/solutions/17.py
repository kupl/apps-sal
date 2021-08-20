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
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                tmp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = tmp
                tmp = aindex[j]
                aindex[j] = aindex[j + 1]
                aindex[j + 1] = tmp
            if b[j] > b[j + 1]:
                tmp = b[j]
                b[j] = b[j + 1]
                b[j + 1] = tmp
                tmp = bindex[j]
                bindex[j] = bindex[j + 1]
                bindex[j + 1] = tmp
    bfinal = list(range(n))
    afinal = list(range(n))
    for i in range(n):
        afinal[aindex[i]] = i + 1
        bfinal[bindex[i]] = i + 1
    '\n    for i in range(n):\n        max=-1\n        maxindex =0\n        for j in range(n):\n            temp=~(a[i]^b[j])\n            if temp>max and c[j]==0:\n                max = temp\n                maxindex=j\n        bindex[maxindex]=i+1          \n        c[maxindex]=1'
    for i in afinal:
        print(i, end=' ')
    print()
    for j in bfinal:
        print(j, end=' ')
    print()
    t = t - 1
