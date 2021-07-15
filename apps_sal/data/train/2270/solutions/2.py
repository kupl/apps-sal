mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, x, y, z = list(map(int, input().split()))
    s = x + y + z
    m = max(x, y, z)
    mask_x = (1 << (x + 1)) - 1
    mask_y = (1 << y) - 1
    mask_z = (1 << z) - 1

    dp = [0] * (1 << s)
    dp[1] = 1
    for _ in range(N):
        dp_new = [0] * (1 << s)
        for state in range(1 << s):
            if dp[state] == 0:
                continue
            state_x = state & mask_x
            state_y = (state >> (x + 1)) & mask_y
            state_z = (state >> (x + y + 1)) & mask_z
            for w in range(1, m+1):
                if z - w - 1 >= 0:
                    if (state_z >> (z - w - 1)) & 1:
                        continue
                if w == z and (state_y >> (y - 1)) & 1:
                    continue
                state_new = ((state_x << w) & mask_x) | (((state_y << w) & mask_y) << (x + 1))\
                            | (((state_z << w) & mask_z) << (x + y + 1)) | 1
                if ((state_x >> x) & 1) and w <= y:
                    state_new |= (1 << (w + x))
                if ((state_y >> (y - 1)) & 1) and w <= z:
                    state_new |= (1 << (w + x + y))
                dp_new[state_new] = (dp_new[state_new] + dp[state])%mod
            dp_new[1] = (dp_new[1] + (dp[state] * (10 - m))%mod)%mod
        dp = dp_new
    ans = pow(10, N, mod)
    for a in dp:
        ans = (ans - a)%mod
    print(ans)


def __starting_point():
    main()

__starting_point()
