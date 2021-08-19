import math
f = math.factorial
for u in range(eval(input())):
    (n, q) = list(map(int, input().split()))
    for j in range(q):
        (i, k) = list(map(int, input().split()))
        if k > i:
            c = 0
            print(c)
        else:
            a = 2 ** (n - i)
            b = 1
            d = int(i - 1)
            e = 1
            h = 1
            g = 1
            if k - 1 > i - k:
                for z in range(i - k):
                    b = b * d
                    d = d - 1
                    e = e * h
                    h = h + 1
                b = b / e
            else:
                for z in range(k - 1):
                    b = b * d
                    d = d - 1
                    e = e * g
                    g = g + 1
                b = b / e
            c = a * b
            c = c % 1000000007
            print(c)
