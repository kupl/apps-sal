T = int(input())
for t in range(0, T):
    n = int(input())
    s = [0] * n
    np = [0] * n
    for i in range(0, n):
        (s[i], np[i]) = input().split()
        np[i] = int(np[i])
    no = np[:]
    no.sort()
    ans = '-1'
    if no[0] != no[1]:
        ans = no[0]
    else:
        for i in range(1, n - 1):
            if no[i] != no[i - 1] and no[i] != no[i + 1]:
                ans = no[i]
                break
            else:
                continue
        if ans == '-1' and no[n - 2] != no[n - 1]:
            ans = no[n - 1]
    for i in range(0, n):
        if ans == np[i]:
            ans = int(i)
            break
    if ans == '-1':
        print('Nobody wins.')
    else:
        print(s[ans])
