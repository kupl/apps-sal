def f():
    n = int(input())
    a = list(map(int, input().split()))
    ind = [] * 1001
    for i in range(0, 1001):
        ind.append([])
    for i in range(0, len(a)):
        ind[a[i]].append(i)
    maxi = 0
    data = 0
    for i in range(1, 1001):
        s = 0
        c = 1
        if len(ind[i]) == 1:
            s = 1
            if maxi < s:
                maxi = s
                data = i
            elif maxi == s:
                data = min(data, i)
            continue
        for j in range(1, len(ind[i])):
            if ind[i][j] - ind[i][j - 1] == 1:
                c += 1
            if ind[i][j] - ind[i][j - 1] != 1:
                s += c // 2 + c % 2
                c = 1
            if j == len(ind[i]) - 1:
                s += c // 2 + c % 2
                c = 1
        if maxi < s:
            maxi = s
            data = i
        elif maxi == s:
            data = min(data, i)
    if len(a) == 1:
        print(a[0])
    else:
        print(data)


for i in range(int(input())):
    f()
