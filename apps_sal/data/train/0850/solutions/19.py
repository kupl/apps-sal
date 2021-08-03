# cook your dish here
# cook your dish here
hm = {}


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_list(l, n):
    gcd1 = l[0]
    for i in range(1, n):
        gcd1 = gcd(gcd1, l[i])
    return gcd1


for _ in range(int(input())):
    n = int(input())
    x = [int(n) for n in input().split()]
    l2 = []
    l = list(set(x))
    n = len(l)
    if n > 2:
        hm = {}
        temp = []
        max1 = max(l[0], l[1])
        max2 = min(l[0], l[1])
        for i in range(2, len(l)):
            if l[i] > max1:
                max2 = max1
                max1 = l[i]
            else:
                if l[i] > max2:
                    max2 = l[i]
        m1 = max1
        m2 = max2
        l.remove(m1)
        l.remove(m2)
        gcd_1 = l[0]
        for i in range(1, n - 2):
            gcd_1 = gcd(gcd_1, l[i])
        s1 = gcd(gcd_1, m2) + m1
        s2 = gcd(gcd_1, m1) + m2
        print(max(s1, s2))
    else:
        if n == 1:
            print(l[0] * 2)
        else:
            print(sum(l))
