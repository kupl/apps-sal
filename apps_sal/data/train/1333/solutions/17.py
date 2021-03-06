def solve(n, b):
    for i in range(n - 1):
        if b[i] & b[i + 1] != b[i]:
            print(0)
            return
    x = 0
    for i in range(n - 1):
        x += bin(b[i]).count('1')
    ans = 1
    while x:
        if x > 30:
            ans *= twopow[30]
            ans %= mod
            x -= 30
        else:
            ans *= twopow[x]
            ans %= mod
            x = 0
    print(ans % mod)


mod = 10 ** 9 + 7
twopow = {x: (1 << x) % mod for x in range(35)}
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    solve(n, b)
