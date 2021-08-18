for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = {}
    for i in range(len(c)):
        d[i + 1] = c[i]
    ans = []
    profit = 0
    r_1 = 0
    for i in range(n):
        t_1, t_2, t_3 = list(map(int, input().split()))
        if d[t_1] > 0:
            profit += t_2
            d[t_1] -= 1
            ans.append(t_1)
        else:
            profit += t_3
            r_1 += 1
            ans.append('')
    print(profit)
    rem = []
    for i in d:
        if d[i] > 0:
            rem += [i] * d[i]
            d[i] = 0
        if len(rem) >= r_1:
            break
    j = 0
    for i in range(len(ans)):
        if ans[i] == '':
            ans[i] = rem[j]
            j += 1
    print(*ans)
