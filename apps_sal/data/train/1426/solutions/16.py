test = int(input())
for _ in range(test):
    n, m = map(int, input().split(" "))
    c = [int(j) for j in input().split(" ")]
    revenue = 0
    finallist = []
    remlist = []
    p = 0
    customer = []
    for j in range(n):
        customer.append([int(j) for j in input().split(" ")])
        if c[customer[j][0] - 1] > 0:
            revenue += customer[j][1]
            finallist.append(customer[j][0])
            c[customer[j][0] - 1] -= 1
        else:
            remlist.append(p)
        p += 1

    k = 0
    while len(remlist):
        if c[k] > 0:
            revenue += customer[remlist[0]][2]
            finallist.insert(remlist[0], k + 1)
            c[k] -= 1
            remlist.remove(remlist[0])
        else:
            k += 1
    print(revenue)
    print(*finallist, sep=" ")
