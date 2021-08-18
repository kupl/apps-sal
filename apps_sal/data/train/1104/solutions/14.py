t = int(input())
mod = 10**9 + 7
for _ in range(t):
    n, k = list(map(int, input().split()))
    if n == 0:
        k -= 1
        print(k**2 + k)
        continue
    if k == 1:
        l = n - 1
        nz = l**2 + l
        print(nz + n)
        continue
    rem = k % 2
    up = k // 2
    l = up + n - 1
    nz = l**2 + l
    if rem == 0:
        ans = nz + n
        print(ans % mod)
    else:
        ans = nz + 2 * l + 2 - n
        print(ans % mod)
