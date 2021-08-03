t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().strip().split()))
    bl = 0
    jod = 0
    big = 0
    for j in l:
        if j < 31:
            bl += 1
        else:
            jod += j
        if j > big:
            big = j
    avg = jod / n
    dif = [0 for i in range(n)]
    top = []
    for j in range(n):
        dif[j] = big - l[j]
        if l[j] == big:
            top.append(j)
    print(bl, end=' ')
    print('%.2f' % avg)
    for j in range(len(top) - 1, -1, -1):
        print(top[j], end=' ')
    print()
    for j in range(n):
        print(dif[j])
