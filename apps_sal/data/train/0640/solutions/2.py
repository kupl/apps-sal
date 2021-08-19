def compute_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def compute_lcm(x, y):
    lcm = x * y // compute_gcd(x, y)
    return lcm


t = int(input())
for i in range(t):
    x_y = input().split()
    x = int(x_y[0])
    y = int(x_y[1])
    if x == y:
        print(0)
    else:
        sweetness = compute_lcm(x, y)
        x = sweetness / x - 1
        y = sweetness / y - 1
        print(int(x + y))
