from sys import stdin
readline = stdin.readline

n = int(readline())

a = list(map(int, readline().split()))
k_max = 1 << n

# 和が最大 => 最大、2番目に大きいものの和
# dp[k] == kを得るときの最大、2番目に大きいもの
# == max(dp[i] | i はkの部分集合)
# kの部分集合は k に1要素足りないものを列挙すれば十分。
# (2要素以上足りないものは1要素足りないものの部分集合なので)
dp = [[a[i], 0] for i in range(k_max)]
for i in range(n):
    bit = (1 << i)  # i bit目に着目
    for src in range(k_max):  # i bit目が0のものからibit目が1のものへ配るDP
        if bit & src:
            continue  # すでにi bit目が1なら無視
        dst = bit | src
        max_values = dp[dst] + dp[src]
        max_values.sort()
        dp[dst] = [max_values[-1], max_values[-2]]

# k以下 => 前回の答え(k未満)とkに等しい時を合わせた結果
ans = 0
for k in range(1, k_max):
    ans = max(ans, dp[k][0] + dp[k][1])
    print(ans)
