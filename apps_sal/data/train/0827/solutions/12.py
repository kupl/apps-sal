T = int(input())
while T != 0:
    T = T - 1
    (N, K) = map(int, input().split())
    S = input()
    S1 = S + S
    sub = 'ab'
    lookup = [[0] * (2 * N + 1) for _ in range(3)]
    for i in range(0, 2 * N + 1):
        lookup[0][i] = 1
    for i in range(1, 2 * N + 1):
        for j in range(1, 3):
            if S1[i - 1] == sub[j - 1]:
                lookup[j][i] = lookup[j - 1][i - 1] + lookup[j][i - 1]
            else:
                lookup[j][i] = lookup[j][i - 1]
    base = lookup[2][N]
    inc = lookup[2][2 * N] - 2 * base
    ans = K * base + (K - 1) * K * inc // 2
    print(ans)
