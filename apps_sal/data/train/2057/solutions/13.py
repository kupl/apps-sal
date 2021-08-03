N = 10**9 + 7
s = input().strip()
n = 0
ret = 0
c2n = 2**n - 1
for c in s:
    if c == 'a':
        n += 1
        c2n = (2 * c2n + 1) % N
    else:
        ret += c2n
        ret %= N
print(ret)
