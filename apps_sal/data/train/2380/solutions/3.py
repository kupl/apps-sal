import sys
strs = iter(sys.stdin.read().split())
ints = (int(x) for x in strs)
sys.setrecursionlimit(3000)


def main():
    ntc = next(ints)
    for tc in range(1, ntc + 1):
        n, k = (next(ints) for i in range(2))
        s = next(strs)
        R = (n + k - 1) // k
        m = [[int(i * k + j < n and s[i * k + j] == '1') for i in range(R)] for j in range(k)]
        s = [sum(m[j]) for j in range(k)]
        s_sum = sum(s)
        ans = [0] * k
        # 0  1  1  0  1  0  1  1  0
        for j in range(k):
            off = [0] * (R + 1)
            on = [0] * (R + 1)
            for i in range(R - 1, -1, -1):
                off[i] = m[j][i] + off[i + 1]
                on[i] = 1 - m[j][i] + min(on[i + 1], off[i + 1])
            for i in range(R + 1):
                off[i] = (i and off[i - 1]) + (i < R and m[j][i])
                on[i] = on[i] + (i and off[i - 1])
            ans[j] = s_sum - s[j] + min(on)
        print(min(ans))
    return


main()
