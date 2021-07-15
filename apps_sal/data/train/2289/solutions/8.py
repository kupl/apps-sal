import sys
input = sys.stdin.readline

S = [ord(s) - ord('a') for s in input().rstrip()]

INF = 10 ** 9
N = len(S)
dp = [None] * (N+1)
# そこから始めたとき、次にxが現れる位置、および、次にxをとった場合に長さLのものが全て作れる
dp[N] = [[INF] * 26, [0] * 26, 0]

for n in range(N-1,-1,-1):
    prev = dp[n+1]
    cur = [prev[0].copy(), prev[1].copy(), prev[2]]
    s = S[n]
    cur[0][s] = n
    cur[1][s] = prev[2] // 26 + 1
    cur[2] = prev[2] + cur[1][s] - prev[1][s]
    dp[n] = cur

answer = []
i = 0
while i < N:
    # 辞書順で、作れる長さが一番短い文字
    L = dp[i][2] // 26
    for x in range(26):
        if dp[i][1][x] == L:
            break
    answer.append(chr(ord('a') + x))
    # その文字の場所に移動
    i = dp[i][0][x]
    i += 1

print(''.join(answer))
