t = int(input())
mod = 10 ** 9 + 7
for _ in range(t):
    (a, b) = list(map(int, input().split()))
    x = a // 2
    d = x * (x + 1)
    ans = pow(b, d, mod)
    print(ans)
