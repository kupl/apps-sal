from collections import defaultdict
n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
ctr = len(set(l))
l.sort()
dic = defaultdict(lambda: 0)
for i in l:
    dic[i] += 1
dic1 = defaultdict(lambda: 0)
index = 1
for i in list(dic.keys()):
    dic1[index] = dic[i]
    index += 1
dp = [[0 for i in range(k + 1)] for j in range(ctr + 1)]


dp[0][0] = 1
for row in range(1, ctr + 1):
    for col in range(k + 1):
        if col == 0:
            dp[row][col] = 1
        else:
            dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1] * dic1[row]

print(sum(dp[ctr]) % 1000000007)
