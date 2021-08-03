for _ in range(int(input())):
    n = int(input())
    x = n // 250000
    c = x * 250000
    r = n - c
    tax = 0
    if n <= 1500000:
        i = 0
        while c > 0:
            tax += i * 12500
            c -= 250000
            i += 1
        t1 = x * 0.05 * r
        tax += t1
    else:
        i = 0
        d = n - 1500000
        k = 1500000
        while k > 0:
            tax += i * 12500
            k -= 250000
            i += 1
        t1 = d * 0.3
        tax += t1
    print(int(n - tax))
