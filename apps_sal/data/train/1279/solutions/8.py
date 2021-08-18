T = int(input())

for _ in range(T):

    res = 0
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        words = input().split()
        X.append(int(words[0]))
        Y.append(int(words[1]))

    d = {}

    for i in range(N):
        if(X[i] not in d.keys()):
            d[X[i]] = []
            d[X[i]].append(Y[i])
        else:
            d[X[i]].append(Y[i])

    sum_lst = []
    for key in d.keys():
        maxi = d[key][0]
        for num in d[key]:
            if(maxi < num):
                maxi = num
        sum_lst.append(maxi)

    if(len(sum_lst) >= 3):
        max1 = max(sum_lst)
        sum_lst.remove(max1)
        max2 = max(sum_lst)
        sum_lst.remove(max2)
        max3 = max(sum_lst)
        res = max1 + max2 + max3
    else:
        res = 0

    print(res)
