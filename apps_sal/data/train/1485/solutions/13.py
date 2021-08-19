t = int(input())
for you in range(t):
    n = int(input())
    lo = []
    for i in range(n):
        l = input()
        li = [int(i) for i in l]
        lo.append(li)
    lrowhalf1 = [0 for i in range(n)]
    lrowhalf2 = [0 for i in range(n)]
    for i in range(n):
        lrowhalf1[i] = sum(lo[i][0:n // 2])
        lrowhalf2[i] = sum(lo[i][n // 2:n])
    mina = abs(sum(lrowhalf1) - sum(lrowhalf2))
    for i in range(n):
        mini = abs(sum(lrowhalf1) - 2 * (lrowhalf1[i] - lrowhalf2[i]) - sum(lrowhalf2))
        if mini < mina:
            mina = mini
    print(mina)
