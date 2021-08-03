t = int(input())
for i in range(t):
    d = []
    f = []
    b = []
    profit = 0

    n, m = [int(x) for x in input().split()]

    order = [0 for j in range(n)]
    flav = [int(x) for x in input().split()]
    for j in range(n):
        inp = [int(x) for x in input().split()]
        d.append(inp[0])
        f.append(inp[1])
        b.append(inp[2])

    for j in range(n):
        if(flav[d[j] - 1]) > 0:
            profit = profit + f[j]
            flav[d[j] - 1] -= 1
            order[j] = d[j]
    flag = 0
    for j in range(n):
        if(order[j] == 0):
            for k in range(flag, n):
                if(flav[flag] > 0):
                    order[j] = flag + 1
                    flav[flag] -= 1
                    profit += b[j]
                    break
                else:
                    flag += 1

    print(profit)
    for k in range(len(order) - 1):
        print(order[k], end=" ")
    print(order[-1])
