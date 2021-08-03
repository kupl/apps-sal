import copy


def calprofit(lines_removed, j):

    lines_set = copy.deepcopy(differentline[j])
    #print("chk", lines_set)
    iterator = 0

    while(iterator < len(lines_set) and lines_removed > 0):

        possible = min(lines_set[iterator], lines_removed)
        lines_set[iterator] = lines_set[iterator] - possible
        lines_removed = lines_removed - possible
        iterator = iterator + 1

        # if lines_removed still remains after deleting all  the lines then no triangle possible

    if(lines_removed > 0):
        return 0
    sum1 = 0
    for iterator1 in range(len(lines_set)):
        sum1 = sum1 + lines_set[iterator1]
    sum2 = 0
    temp = [0] * (len(lines_set) + 1)
    for iterator2 in range(len(lines_set)):
        temp[iterator2] = lines_set[iterator2] * (sum1 - lines_set[iterator2])
        sum2 = sum2 + temp[iterator2]
    sum2 = sum2 // 2
    sum3 = 0
    for iterator3 in range(len(lines_set)):
        sum3 = sum3 + lines_set[iterator3] * (sum2 - temp[iterator3])
    sum3 = sum3 // 3
    # print(sum3)
    return sum3


for i in range(int(input())):
    n, c, k = [int(i) for i in input().split()]
    color = []
    for i in range(c + 1):
        color.append(dict())
    for i in range(n):
        a, b, co = [int(i) for i in input().split()]
        if(color[co].get(a, 0)):
            color[co][a] = color[co][a] + 1
        else:
            color[co][a] = 1
    differentline = []
    for i in color:
        chk = list(i.values())
        chk.sort()
        differentline.append(chk)

    # print(differentline)

    weight = [0] + [int(i) for i in input().split()]

    ##  KNAPSACK   ##
    profit = []
    dp = []

    for i in range(k + 1):
        profitdemo = []
        dpdemo = []
        for j in range(c + 1):
            profitdemo.append(-1)

            if(j == 0):
                dpdemo.append(0)
            else:
                dpdemo.append((10**20) + 7)
        profit.append(profitdemo)
        dp.append(dpdemo)

    for i in range(k + 1):
        for j in range(1, c + 1):
            removable_item = i // weight[j]
            for lines_removed in range(removable_item + 1):
                demo = lines_removed * weight[j]

                # calculting profit  ## after removing lines_removed number of lines from color of j
                if(profit[lines_removed][j] == -1):
                    profit[lines_removed][j] = calprofit(lines_removed, j)

                dp[i][j] = min(dp[i][j], dp[i - demo][j - 1] + profit[lines_removed][j])
    print(dp[k][c])
