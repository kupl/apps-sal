import math


def lcm(s, s1):
    mul = s * s1
    gcd = math.gcd(s, s1)
    lcm = mul // gcd
    return lcm


def __starting_point():
    t = int(input())
    while t > 0:
        t = t - 1
        N = int(input())
        num_array = list(map(int, input().split(' ')[:N]))
        l = num_array[0]
        for i in range(1, N):
            l = lcm(l, num_array[i])
        r = int(input())
        print(l + int(r))


__starting_point()
