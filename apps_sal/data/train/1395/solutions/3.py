from math import sqrt


def get_factors(n):
    f = 0
    for i in range(1, int(sqrt(n)) + 1):
        if(n % i == 0):
            f += 1
            if(i != n // i):
                f += 1
    return f


T = int(input())
ans = []

for _ in range(T):
    A, B = [int(i) for i in input().split()]

    x = A - 1
    y = B - 1

    ans.append(get_factors(abs(x - y)))

for i in ans:
    print(i)
