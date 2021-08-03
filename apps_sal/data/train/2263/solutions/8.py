M = 998244353
s = input()
n = len(s) - 1
v = sum(map(ord, s))
r = pow(3, n, M) - pow(2, n, M) + pow(2, n // 3, M) * (n % 3 == 2) * (1 - 3 * (v % 3 == 0)) + all(s[i] != s[i + 1]for i in range(n)) - (v == 294)
if all(s[0] == k for k in s):
    r = 1
print(r % M)
