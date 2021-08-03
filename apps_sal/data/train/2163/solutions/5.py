import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    MOD = int(1e9 + 7)
    was = set()
    s = list(map(int, minp()))
    n = len(s)

    first, last = None, None

    for i in range(n):
        v = s[i]
        if v == 1:
            first = i
            break
    if first is None:
        print(n)
        return

    dp = [0] * n
    dp[first] = 1
    st = []
    stv = []
    r = 0
    i = first
    while i < n:
        j = i + 1
        while j < n and s[j] == 0:
            j += 1
        r = (r + dp[i]) % MOD
        if j == n:
            last = i
            break
        c = j - i - 1
        add = 0
        st.append(0)
        stv.append(dp[i])
        while len(st) > 0 and st[-1] <= c:
            v = st.pop()
            d = stv.pop()
            dp[j] = (dp[j] + d * (c - v + 1)) % MOD
            add += d
        if len(st) > 0 and st[-1] == c + 1:
            stv[-1] = (stv[-1] + add) % MOD
        else:
            st.append(c + 1)
            stv.append(add)
        i = j
    print((r * (first + 1) * (n - last)) % MOD)


solve()
