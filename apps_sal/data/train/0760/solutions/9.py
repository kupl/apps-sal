import sys


def extended_gcd(aa, bb):
    (lastremainder, remainder) = (abs(aa), abs(bb))
    (x, lastx, y, lasty) = (0, 1, 1, 0)
    while remainder:
        (lastremainder, (quotient, remainder)) = (remainder, divmod(lastremainder, remainder))
        (x, lastx) = (lastx - quotient * x, x)
        (y, lasty) = (lasty - quotient * y, y)
    return (lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1))


def modinv(a, m):
    (g, x, y) = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


(aa, bb, mod) = (500, 300, 10 ** 9 + 7)
fact = [1]
for i in range(1, pow(10, 5) + 10):
    fact.append(fact[i - 1] * i % mod)
for _ in range(int(sys.stdin.readline())):
    s = list(map(str, sys.stdin.readline().split()))[0]
    ch = [0] * 26
    for i in s:
        ch[ord(i) - 97] += 1
    n = len(s)
    (ans, zero) = (0, 1)
    total = fact[n]
    for i in range(26):
        if ch[i] > 0:
            total = total * modinv(fact[ch[i]], mod) % mod
    for i in range(26):
        if ch[i] > 0:
            for j in range(i + 1, 26):
                if ch[j] > 0:
                    ans = (ans + ch[i] * ch[j]) % mod
                    ans = (ans + ch[i] * ch[j] % mod * (ch[i] - 1) % mod * (ch[j] - 1) % mod * 250000002 % mod) % mod
                    for k in range(j + 1, 26):
                        if ch[k] > 0:
                            ans = (ans + ch[i] * ch[j] % mod * ch[k] % mod * 2 % mod) % mod
                            ans = (ans + ch[i] * ch[j] % mod * ch[k] % mod * (ch[i] - 1) % mod) % mod
                            ans = (ans + ch[i] * ch[j] % mod * ch[k] % mod * (ch[j] - 1) % mod) % mod
                            ans = (ans + ch[i] * ch[j] % mod * ch[k] % mod * (ch[k] - 1) % mod) % mod
                            for l in range(k + 1, 26):
                                if ch[l] > 0:
                                    ans = (ans + ch[i] * ch[j] % mod * ch[k] % mod * ch[l] % mod * 3 % mod) % mod
    print((pow(total, 2, mod) - (ans + zero) % mod * total % mod % mod) % mod)
