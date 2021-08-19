import math


def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = []
    sm = []
    p1 = 0
    p2 = 0
    j = 0
    while j < n - 1:
        if gcd(a[j], a[j + 1]) != 1:
            p1 = j + 0
            while j < n - 1 and gcd(a[j], a[j + 1]) != 1:
                j += 1
            p2 = j + 0
            l.append([p1, p2])
            sm.append(p2 - p1 + 1)
        else:
            j += 1
    if len(l) > 0 and l[0][1] - l[0][0] < n - 1:
        if l[-1][1] == n - 1 and l[0][0] == 0:
            if gcd(a[-1], a[0]) != 1:
                sm[0] += sm[-1]
                sm.pop()
        elif gcd(a[-1], a[0]) != 1 and l[0][0] == 0:
            sm[0] += 1
        elif gcd(a[-1], a[0]) != 1 and l[-1][1] == n - 1:
            sm[-1] += 1
        elif gcd(a[-1], a[0]) != 1:
            sm.append(2)
        w = [0] * (n + 1)
        for j in range(len(sm)):
            for k in range(2, sm[j] + 1):
                w[k] += math.ceil((sm[j] - 1) // (k - 1))
        print(*w[2:])
    elif len(l) > 0:
        w = [0] * (n + 1)
        if gcd(a[-1], a[0]) != 1:
            for j in range(len(sm)):
                for k in range(2, sm[j] + 1):
                    w[k] += math.ceil((sm[j] - 1) // (k - 1)) + 1
            print(*w[2:])
        else:
            for j in range(len(sm)):
                for k in range(2, sm[j] + 1):
                    w[k] += math.ceil((sm[j] - 1) // (k - 1))
            print(*w[2:])
    else:
        w = [0] * (n + 1)
        if gcd(a[-1], a[0]) != 1:
            w[2] = 1
            print(*w[2:])
        else:
            print(*w[2:])
