

MOD = 1000000007


def powmod(base, exp):
    if exp == 0:
        return 1
    elif exp & 1:
        return (base * powmod(base, exp - 1)) % MOD
    else:
        return powmod((base * base) % MOD, exp // 2) % MOD


t = eval(input())
for i in range(0, int(t)):
    n = eval(input())
    k = int(n) // 2
    if (int(n) & 1):
        result = 3 * (powmod(9, k) - 1)
    else:
        result = powmod(9, k) + 3
    print(result % MOD)
