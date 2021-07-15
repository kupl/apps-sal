T = input()
mod = int(1e9 + 7)
a = map(int, input().split())
c = []
for n in a:
    b = (n // 2 + 2)
    b = b * b
    b //= 4
    c.append(str(b % mod))
print(' '.join(c))
