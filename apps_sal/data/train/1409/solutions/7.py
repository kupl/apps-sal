def gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    return x * y // gcd(x, y)


abc = 'abcdefghijklmnopqrstuvwxyz'
pi = 3.141592653589793
t = int(input())
for _ in range(t):
    n = int(input())
    bin_n = bin(n)[2:]
    print(bin_n.count('1'))
