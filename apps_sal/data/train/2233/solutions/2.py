T = input()
mod = int(1000000000.0 + 7)
a = list(map(int, input().split()))
c = []
for n in a:
    b = n // 2 + 2
    b = b * b
    b //= 4
    c.append(str(b % mod))
print(' '.join(c))
