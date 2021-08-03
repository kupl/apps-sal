for t in range(int(input())):
    n = int(input()) // 2
    s = input()
    d = {}
    for i in s:
        if (i not in d):
            d[i] = 0
        d[i] += 1
    res = 0
    for i in d:
        if (d[i] % 2):
            res += 1
    if (n % 2):
        if (res == 0 or res == 2):
            print("YES")
        else:
            print("NO")
    else:
        if (res == 0):
            print("YES")
        else:
            print("NO")
