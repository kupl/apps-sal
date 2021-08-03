def read(): return list(map(int, input().split()))
def per(L, R): return R - L - 1 + min(R - n - 1, n - L)


n, a, b, T = read()
f = [1 + (i == 'w') * b for i in input()] * 2
L, R = 0, n
ans = 0
cur = sum(f) // 2
while L <= n and R < n * 2:
    cur += f[R]
    R += 1
    while R - L > n or cur + per(L, R) * a > T:
        cur -= f[L]
        L += 1
    ans = max(ans, R - L)
print(ans)
