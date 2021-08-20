T = int(input())
while T > 0:
    (n, p) = input().split()
    n = int(n)
    p = int(p)
    if n > 2:
        Rem = n % (n // 2 + 1)
        total = (p - Rem) * (p - Rem) + (p - n) * (p - Rem) + (p - n) * (p - n)
    else:
        total = p * p * p
    print(total)
    T = T - 1
