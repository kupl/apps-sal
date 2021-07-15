memo, N, MOD = [0], 10000, 12345787

def three_by_n(n):
    if len(memo) <= N:
        dp = [[0] * (1<<4) for _ in range(2)]
        crt, nxt = dp[0], dp[1]
        crt[0] = 1
        for x in range(N-1, -1, -1):
            for y in range(3-1, -1, -1):
                for used in range(1 << 4):
                    if (used >> y) & 1:
                        nxt[used] = crt[used & ~(1 << y)]
                    else:
                        res = crt[used | 1 << (y+1)] if y+1 < 3 and not(used >> (y+1) & 1) else 0
                        res += crt[used | (1 << y)] if x+1 < N else 0
                        if (used >> 3):
                            nxt[used] = (nxt[used] + res) % MOD
                        else:
                            nxt[used] = res % MOD
                            nxt[used | 1 << 3] = crt[used & ~(1 << y)]
                crt, nxt = nxt, crt
            memo.append(crt[0] if x % 2 == 0 else crt[1<<3])
    return memo[n]
