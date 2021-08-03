m = [1]
mod = 10**9 + 7
for i in range(60):
    a = m[-1]
    a *= 2
    a %= mod
    m.append(a)

for i in range(int(input())):
    L, R = map(int, input().split())
    tmp = 0
    l = bin(L)[2:]
    r = bin(R)[2:]
    a = 1
    ans = L % mod
    for i in range(1, len(l) + 1):
        if(l[-i] == '0'):
            if tmp + 2**(i - 1) <= R - L:
                ans += ((m[i - 1]) * (L - a + 1)) % mod
                tmp += 2**(i - 1)
                ans %= mod
            else:
                ans += ((R - L - tmp) * (L - a + 1)) % mod
                ans %= mod
                break
        else:
            a += m[i - 1]
    print(ans)
