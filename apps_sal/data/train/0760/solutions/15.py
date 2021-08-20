def power(a, b):
    modu = 1000000007
    res = 1
    while b > 0:
        if b & 1 != 0:
            res = res * a % modu
        a = a * a % modu
        b >>= 1
    return res


modu = 1000000007
factorial = [0] * 100010
factorial[0] = 1
for i in range(1, 100010):
    factorial[i] = factorial[i - 1] * i % modu
test = int(input())
for tst in range(test):
    has = [0] * 30
    st = input()
    for i in st:
        has[ord(i) - ord('a')] += 1
    neeche = 1
    for i in range(26):
        neeche = neeche * factorial[has[i]] % modu
    final = factorial[len(st)] * power(neeche, modu - 2) % modu
    minus = 1
    for i in range(26):
        for j in range(i + 1, 26):
            minus = (minus + has[i] * has[j]) % modu
    for i in range(26):
        for j in range(i + 1, 26):
            for k in range(j + 1, 26):
                minus = (minus + has[i] * has[j] * has[k] * 2) % modu
    mul = 0
    for i in range(26):
        for j in range(i + 1, 26):
            for k in range(0, 26):
                if k != i and k != j:
                    for l in range(k + 1, 26):
                        if l != i and l != j:
                            mul = (mul + has[i] * has[j] * has[k] * has[l]) % (2 * modu)
    mul /= 2
    minus = (minus + mul) % modu
    mul = 0
    for i in range(26):
        if has[i] > 1:
            for j in range(26):
                if j != i:
                    for k in range(j + 1, 26):
                        if k != i:
                            mul = (mul + has[i] * (has[i] - 1) / 2 * has[j] * has[k]) % modu
    minus = (minus + mul * 2) % modu
    mul = 0
    for i in range(26):
        for j in range(i + 1, 26):
            if has[i] >= 2 and has[j] >= 2:
                mul = (mul + has[i] * (has[i] - 1) / 2 * (has[j] * (has[j] - 1) / 2)) % modu
    minus = (minus + mul) % modu
    mul = final - minus
    if mul < 0:
        mul += modu
    ans = final * mul % modu
    print(ans)
