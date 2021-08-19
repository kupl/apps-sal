# cook your dish here
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // (gcd(x, y))


abc = "abcdefghijklmnopqrstuvwxyz"

pi = 3.141592653589793238

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    comm = lcm(x, y)
    x_n = comm // x - 1
    y_n = comm // y - 1
    print(x_n + y_n)
