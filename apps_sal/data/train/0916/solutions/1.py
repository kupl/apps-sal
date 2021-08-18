def compute_gcd(x, y):

    while(y):
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    lcm = (x * y) // compute_gcd(x, y)
    return lcm


for _ in range(int(input())):
    a = [int(i) for i in input().split()]
    print(compute_lcm(a[0], a[1]))
