for t in range(int(input())):
    n = int(input())
    ans = [2] * n
    d = list(map(int, input()))
    k = d[0]
    ind_1 = -1
    for i in range(n):
        if d[i] > k:
            k = d[i]
        if d[i] < k:
            ans[i] = 1
            if ind_1 == -1:
                ind_1 = i
    for i in range(ind_1):
        if d[i] <= d[ind_1]:
            ans[i] = 1
    itog = []
    for i in range(n):
        if ans[i] == 1:
            itog.append(d[i])
    for i in range(n):
        if ans[i] == 2:
            itog.append(d[i])
    for i in range(1, n):
        if itog[i] < itog[i - 1]:
            print('-')
            break
    else:
        print(''.join(map(str, ans)))
