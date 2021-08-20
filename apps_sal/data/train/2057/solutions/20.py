MOD = 1000000000.0 + 7
s = input()
ans = 0
b = 0
for c in s[::-1]:
    if c == 'a':
        ans = (ans + b) % MOD
        b = 2 * b % MOD
    else:
        b = (b + 1) % MOD
print(int(ans))
