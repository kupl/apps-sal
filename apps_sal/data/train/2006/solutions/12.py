from fractions import gcd
n, f, m = int(input()), 0, 0
for x in map(int, input().split()):
    f, m = gcd(f, x), max(m, x)
print('Alice' if (m // f - n) % 2 else 'Bob')

