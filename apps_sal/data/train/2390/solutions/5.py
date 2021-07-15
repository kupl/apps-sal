for i in range(int(input())):
    n = int(input())
    sort_col = [0] * (n + 1)
    col_csort = [0] * (n + 1)
    t = 0
    for el in map(int, input().split()):
        col_csort[sort_col[el]] -= 1
        sort_col[el] += 1
        col_csort[sort_col[el]] += 1
        t = max(sort_col[el], t)
    cou = 0
    for j in range(t, 0, -1):
        if col_csort[j]:
            cou += j
            col_csort[j] -= 1
            if col_csort[j]:
                col_csort[j - 1] += col_csort[j]
    print(cou)

