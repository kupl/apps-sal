try:
    for _ in range(int(input())):
        (M, N) = map(int, input().split())
        dp = []
        for i in range(M):
            l = input()
            l = l.replace(' ', '')
            l = l.upper()
            dp.append(list(l))
        pos = []
        for i in range(M):
            if (i + 1) % 2 != 0:
                for j in range(0, N, 1):
                    if dp[i][j] == 'P':
                        pos.append([i, j])
            else:
                for j in range(N - 1, -1, -1):
                    if dp[i][j] == 'P':
                        pos.append([i, j])
        s = 0
        for i in range(len(pos) - 1):
            for j in range(len(pos[i])):
                s += abs(pos[i][j] - pos[i + 1][j])
        print(s)
except:
    pass
