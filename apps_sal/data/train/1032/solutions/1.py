mod = 1000003
fact = [0] * mod
fact[0] = 1
for i in range(1, mod):
    fact[i] = fact[i - 1] * i % mod
t = int(input())
while t:
    t = t - 1
    s = input().split()
    n = int(s[0])
    x = int(s[1])
    if n >= mod:
        print(0)
    else:
        x = x % mod
        ans = fact[n]
        ans = ans * x % mod
        print(ans)
