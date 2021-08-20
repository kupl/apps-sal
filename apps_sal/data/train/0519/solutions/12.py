import bisect


def recur(s_i, e_i, end_i):
    inside = 0
    for i in range(s_i + 1, e_i):
        if b_l[i] < k:
            bi_i = bisect.bisect_left(b_inv[b_l[i] + k], i)
            for ind in b_inv[b_l[i] + k][bi_i:]:
                if i < ind < e_i:
                    dp[i][e_i] = recur(i, ind, e_i)
                    inside = max(inside, dp[i][e_i])
    outside = 0
    for i in range(e_i + 1, min(n, end_i)):
        if b_l[i] < k:
            bi_i = bisect.bisect_left(b_inv[b_l[i] + k], i)
            for ind in b_inv[b_l[i] + k][bi_i:]:
                if i < ind < end_i:
                    dp[i][end_i] = recur(i, ind, end_i)
                    outside = max(outside, dp[i][end_i])
    return v_l[s_i] + v_l[e_i] + outside + inside


(n, k, *l) = map(int, input().split())
(v_l, b_l) = (l[:n], l[n:])
b_inv = {key: [] for key in range(2 * k)}
for i in range(n):
    b_l[i] -= 1
    b_inv[b_l[i]].append(i)
dp = [{} for _ in range(n)]
ans = 0
for i in range(n):
    if b_l[i] < k:
        bi_i = bisect.bisect_left(b_inv[b_l[i] + k], i)
        for ind in b_inv[b_l[i] + k][bi_i:]:
            if i < ind:
                dp[i][n + 1] = recur(i, ind, n + 1)
                ans = max(ans, dp[i][n + 1])
print(ans)
