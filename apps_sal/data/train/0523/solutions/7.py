# cook your dish here

from itertools import combinations


for i in range(int(input())):

    n, k = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    arr.sort()

    sub = [arr[i] for i in range(1, n - 1)]

    comb = combinations(sub, k - 2)

    prod = 1

    # print(list(comb))

    for i in list(comb):

        maximum = max(i)

        minimum = min(i)

        ind_max, ind_min = arr.index(maximum), arr.index(minimum)

        aftermax = n - ind_max - 1

        beforemin = ind_min

        temp = aftermax * beforemin

        for j in i:

            prod = prod * (j**temp)

    print(prod % (10**9 + 7))
