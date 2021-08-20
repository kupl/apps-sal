def compute_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def f_lcm(x, y):
    lcm = x * y // compute_gcd(x, y)
    return lcm


t = int(input().strip())
for i in range(t):
    res = 0
    x_y = [int(i) for i in input().split()]
    x = x_y[0]
    y = x_y[1]
    lcm = f_lcm(x, y)
    temp = lcm
    if x == y:
        print(0)
    else:
        res += lcm // x - 1
        res += lcm // y - 1
        print(res)
