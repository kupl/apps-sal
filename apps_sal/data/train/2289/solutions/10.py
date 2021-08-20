def next_position(S):
    """
    閉区間 (i,N-1] の中の最も左端にあるアルファベットsのindex
    """
    N = len(S)
    next_pos = [[N + 1] * 26 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for s in range(26):
            next_pos[i][s] = next_pos[i + 1][s]
        next_pos[i][ord(S[i]) - ord('a')] = i + 1
    return next_pos


S = input().rstrip()
N = len(S)
next_pos = next_position(S)
dp = [1 << 32] * (N + 2)
dp[-1] = 0
recover = [0] * (N + 1)
for i in range(N, -1, -1):
    for s in range(25, -1, -1):
        if dp[next_pos[i][s]] + 1 <= dp[i]:
            dp[i] = dp[next_pos[i][s]] + 1
            recover[i] = (next_pos[i][s], s)
res = []
i = 0
while i < N:
    (i, s) = recover[i]
    res.append(chr(s + ord('a')))
print(''.join(res))
