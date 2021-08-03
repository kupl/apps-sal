from math import acos, sqrt
t = int(input())


def distance(x, y, p, q):
    a = abs(x - y)
    b = sqrt((p - x)**2 + q**2)
    c = sqrt((p - y)**2 + q**2)
    angle = acos((c ** 2 + b ** 2 - a ** 2) / (2 * b * c))
    return angle


def main():
    for _ in range(t):
        n = int(input())
        c = [int(x) for x in input().split()]
        p, q = map(int, input().split())
        c.sort()
        l = 0
        h = n - 1
        sum1 = 0
        while l < h:
            angle = distance(c[l], c[h], p, q)
            sum1 += angle
            l += 1
            h -= 1
        print(sum1)


def __starting_point():
    main()


__starting_point()
