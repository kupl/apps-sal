from math import factorial
try:
    test_cases = int(input())
    while test_cases:
        test_cases = test_cases - 1
        n = int(input())
        cakes = list(map(int, input().split()))
        sum_of_digits = sum(cakes)
        mul = factorial(n) / n
        base = sum_of_digits * mul
        totalsum = 0
        for k in range(n):
            totalsum += base * 10 ** k
        print(int(totalsum))
except:
    pass
