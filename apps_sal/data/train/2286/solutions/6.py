import sys
readline = sys.stdin.readline

INF = 10**9 + 7


def calc(n, k):
    if k == 1:
        return n
    if n > 20:
        return INF
    return min(INF, (pow(k, n) - 1) // (k - 1))


K, N = list(map(int, readline().split()))

if K % 2 == 0:
    ans = [K // 2] + [K] * (N - 1)
    print((*ans))
else:
    ans = []
    cnt = 0
    half = True
    for l in range(N, 0, -1):
        clk = calc(l, K)
        if half:
            c = 1 + K // 2
            if l % 2 == 0:
                cnt += 1
            if clk // 2 == cnt:
                ans.append(c)
                break
            if clk // 2 < cnt:
                c -= 1
                half = False
                cnt -= clk // 2 + 1

                while cnt >= clk:
                    cnt -= clk
                    c -= 1
                if cnt == clk - 1:
                    ans.append(c)
                    break
        else:
            c = K
            while cnt >= clk:
                cnt -= clk
                c -= 1
            if cnt == clk - 1:
                ans.append(c)
                break
        ans.append(c)
    print((*ans))
