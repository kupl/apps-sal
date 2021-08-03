t = int(input())


def gcd(a, b):

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


for _ in range(t):
    int_1, int_2 = list(map(int, input().split()))

    hcf = gcd(int_1, int_2)

    lcm = (int_2 * int_1) / hcf

    print(int(hcf), int(lcm))
