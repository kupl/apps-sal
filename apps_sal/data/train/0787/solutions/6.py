t = int(input())

for each in range(t):
    a = input()
    n = len(a)

    picks = [0] * (n + 1)
    picks[n - 1] = 1 if (a[n - 1] == '0') else 0
    i = n - 2
    while(i > -1):
        picks[i] = picks[i + 1]
        if (a[i] == '0' and a[i + 1] == '1'):
            picks[i] += 1
        i -= 1
    # print(picks)

    disp = [0] * (n + 1)
    soldiers = 0
    i = n - 1
    while(i > -1):
        if (a[i] == '1'):
            disp[i] = n - soldiers - 1 - i
            soldiers += 1
        i -= 1
    # print(disp)

    ans = 0
    for i in range(n):
        if (a[i] == '1'):
            ans += picks[i] + disp[i]
    print(ans)
