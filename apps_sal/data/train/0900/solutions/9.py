t = int(input())


def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        r = power(a, n // 2)
        if n % 2 == 0:
            return r * r
        else:
            return r * a * r


for i in range(t):
    k = int(input())
    print(10 * power(2, k - 1))
