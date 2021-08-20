from sys import stdin, stdout
mod = 1000 * 1000 * 1000 + 7
for i in range(int(stdin.readline())):
    (l, r) = map(int, stdin.readline().split())
    act = 0
    req = 0
    ans = 0
    for i in range(60):
        val = min(r - l + 1, req - act + 1)
        val %= mod
        if l & 1 << i:
            ans += val * ((1 << i) % mod) % mod
            ans %= mod
            act += 1 << i
        req += 1 << i
    print(ans)
