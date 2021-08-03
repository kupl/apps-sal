from math import sqrt


def per(n):
    if n in diz:
        return diz[n]
    else:
        counter = pow(2, n, m)
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                counter -= per(i)
                if i != 1 and i != (n // i):
                    counter -= per(n // i)
                counter %= m
        return counter


n, m = map(int, input().split())
diz = {1: 2}
print(per(n))
counter = pow(2, n, m)
