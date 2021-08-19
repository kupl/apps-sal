# cook your dish here
mod = 10 ** 8 + 7


def dic_add(dic, k1, v):
    if k1 <= k:
        if k1 in dic:
            dic[k1] = (dic[k1] + v) % mod
        else:
            dic[k1] = v


for _ in range(int(input())):
    n, m, k = list(map(int, input().split()))
    a_l = list(map(int, input().split()))
    b_l = list(map(int, input().split()))

    # 0: m end, 1: n end
    f_dp = [[[{} for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(2)]

    f_dp[0][1][0] = {1: 1}
    f_dp[1][0][1] = {1: 1}
    dif = 1
    for j in range(1, m):
        if b_l[j] != b_l[j - 1]:
            dif += 1
        f_dp[0][j + 1][0] = {dif: 1}

    dif = 1
    for i in range(1, n):
        if a_l[i] != a_l[i - 1]:
            dif += 1
        f_dp[1][0][i + 1] = {dif: 1}

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # m end
            if j - 2 >= 0 and b_l[j - 1] != b_l[j - 2]:
                addi = 1
            else:
                addi = 0
            for kk, vv in list(f_dp[0][j - 1][i].items()):
                dic_add(f_dp[0][j][i], kk + addi, vv)

            if b_l[j - 1] != a_l[i - 1]:
                addi = 1
            else:
                addi = 0
            for kk, vv in list(f_dp[1][j - 1][i].items()):
                dic_add(f_dp[0][j][i], kk + addi, vv)

            # n end
            if i - 2 >= 0 and a_l[i - 1] != a_l[i - 2]:
                addi = 1
            else:
                addi = 0
            for kk, vv in list(f_dp[1][j][i - 1].items()):
                dic_add(f_dp[1][j][i], kk + addi, vv)

            if b_l[j - 1] != a_l[i - 1]:
                addi = 1
            else:
                addi = 0
            for kk, vv in list(f_dp[0][j][i - 1].items()):
                dic_add(f_dp[1][j][i], kk + addi, vv)

    ans = 0
    if k in f_dp[0][m][n]:
        ans += f_dp[0][m][n][k]
    if k in f_dp[1][m][n]:
        ans += f_dp[1][m][n][k]
    print(ans % mod)
