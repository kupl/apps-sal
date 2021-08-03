factorial, mod = [1], 10 ** 9 + 7
for i in range(1, 112345):
    factorial.append(factorial[-1] * i)
    factorial[-1] %= mod

for _ in range(eval(input())):
    X = [0 for i in range(26)]
    for x in input():
        X[ord(x) - ord('a')] += 1
    ans = 1
    for i in range(26):
        for j in range(i + 1, 26):
            ans += X[i] * X[j]
    for i in range(26):
        for j in range(i + 1, 26):
            for k in range(j + 1, 26):
                ans += X[i] * X[j] * X[k] * 2
    for i in range(26):
        for j in range(i + 1, 26):
            ans += (X[i] * (X[i] - 1) * X[j] * (X[j] - 1)) / 4
    for i in range(26):
        for j in range(i + 1, 26):
            for k in range(j + 1, 26):
                ans += ((X[i] * X[j] * X[k]) * (X[i] + X[j] + X[k] - 3))
    for i in range(26):
        for j in range(i + 1, 26):
            for k in range(j + 1, 26):
                for l in range(k + 1, 26):
                    ans += X[i] * X[j] * X[k] * X[l] * 3
    stuff = factorial[sum(X)]
    for x in X:
        if x:
            stuff *= pow(factorial[x], mod - 2, mod)
    stuff %= mod
    print(stuff * (stuff - ans) % mod)
