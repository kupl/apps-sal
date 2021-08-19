t = int(input())
for _ in range(t):
    (n, p, q) = list(map(int, input().split(' ')))
    l = list(map(int, input().split(' ')))
    l.sort()
    s = sum(l)
    a = p + 2 * q
    b = 0
    for i in l:
        if p == 0:
            if i % 2 == 0 and a >= i:
                a = a - i
                b = b + 1
        elif q == 0:
            if a >= i:
                a = a - i
                b = b + 1
        elif i % 2 == 0 and a >= i:
            a = a - i
            b = b + 1
        elif i % 2 != 0 and p != 0 and (a >= i):
            a = a - i
            b = b + 1
            p = p - 1
    print(b)
