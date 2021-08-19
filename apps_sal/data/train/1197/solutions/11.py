t = int(input())
for _ in range(t):
    n = int(input())
    total = 1
    coins = [1]
    sums = set([2])
    num = 2
    while len(coins) < n:
        notIn = True
        if 2 * num not in sums:
            sumx = set()
            for i in coins:
                if i + num not in sums:
                    sumx.add(i + num)
                else:
                    notIn = False
                    break
            if notIn:
                sumx.add(2 * num)
                sums = sums.union(sumx)
                # print(sums)
                coins.append(num)
        num += 1
    for i in coins:
        print(i, end=" ")
    print("\n" + str(sum(coins)))
