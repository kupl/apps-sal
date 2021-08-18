import bisect


def recur(s_i, e_i, end_i):
    if end_i in dp[s_i] and e_i in dp[s_i][end_i]:
        return dp[s_i][end_i][e_i]

    inside = 0
    for i in range(s_i + 1, e_i):
        if b_l[i] < k:
            bi_i = bisect.bisect_left(b_inv[b_l[i] + k], i)
            for ind in b_inv[b_l[i] + k][bi_i:]:
                if i < ind < e_i:
                    inside = max(inside, recur(i, ind, e_i))
    outside = 0
    for i in range(e_i + 1, min(n, end_i)):
        if b_l[i] < k:
            bi_i = bisect.bisect_left(b_inv[b_l[i] + k], i)
            for ind in b_inv[b_l[i] + k][bi_i:]:
                if i < ind < end_i:
                    outside = max(outside, recur(i, ind, end_i))
    if end_i not in dp[s_i]:
        dp[s_i][end_i] = {}
    dp[s_i][end_i].update({e_i: v_l[s_i] + v_l[e_i] + outside + inside})
    return dp[s_i][end_i][e_i]


n, k, *l = map(int, input().split())
v_l, b_l = l[:n], l[n:]

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
                ans = max(ans, recur(i, ind, n + 1))
print(ans)
