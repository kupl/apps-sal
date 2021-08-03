
t = int(input())
mod = 10**9 + 7
for i in range(t):
    n = int(input())
    ans = 0
    for j in range(n + 1):
        temp1 = pow(3, j, mod)
        temp2 = (pow(2, n + 1 - j, mod) + (mod - 1)) % mod
        temp3 = (temp1 * temp2) % mod
        ans = (ans + temp3) % mod
    print(ans)
