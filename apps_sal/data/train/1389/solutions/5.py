def REPLACE(string, par): return ''.join(string.split(par))


out = []
n = int(input())
for _ in range(n):
    s = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(input(), ';'), ':'), ','), '.'), "'")
    out.append(' '.join(s.split()[::-1]))
print(''.join([out[n - (i + 1)] + '\n' for i in range(n)]))

