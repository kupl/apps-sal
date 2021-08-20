mod = 1000000007
for _ in range(int(input())):
    string = list(input().strip())
    idx = 1
    lev = 1
    for i in string:
        if i == 'l':
            if lev % 2 == 1:
                idx = idx * 2
            else:
                idx = idx * 2 - 1
        elif lev % 2 == 1:
            idx = idx * 2 + 2
        else:
            idx = idx * 2 + 1
        lev += 1
        idx = idx % mod
    print(idx)
