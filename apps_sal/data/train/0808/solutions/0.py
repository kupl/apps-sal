from fractions import gcd
for testCases in range(eval(input())):
    n = eval(input())
    if n == 1:
        print('1')
    elif n == 2:
        print('2')
    elif n == 3:
        print('6')
    else:
        c = n * (n - 1)
        k = n - 2
        while True:
            if gcd(k, n - 1) == 1 and gcd(k, n) == 1:
                break
            k -= 1
        d = (n - 1) * (n - 2)
        k1 = n - 3
        while True:
            if gcd(k1, n - 1) == 1 and gcd(k1, n - 2) == 1:
                break
            k1 -= 1
        print(max(c * k, d * k1))
