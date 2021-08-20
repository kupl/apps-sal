s = input()[::-1]
(a, b) = (0, 0)
mod = 10 ** 9 + 7
for i in s:
    if i == 'b':
        b += 1
    else:
        a += b
        a %= mod
        b <<= 1
        b %= mod
print(a)
