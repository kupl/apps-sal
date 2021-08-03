s = input()
mod = 10 ** 9 + 7
b = 0
res = 0
for c in s[::-1]:
    if c == 'b':
        b += 1
    else:
        res += b
        b *= 2
        res %= mod
        b %= mod
print(res)
