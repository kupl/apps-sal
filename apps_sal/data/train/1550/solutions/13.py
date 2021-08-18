def togglebit(n):
    if (n == 0):
        return 1

    i = n

    n |= n >> 1

    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return i ^ n


def xnor(num1, num2):
    if (num1 < num2):
        temp = num1
        num1 = num2
        num2 = temp
    num1 = togglebit(num1)

    return num1 ^ num2


def xn(a, b, n):
    f = [0] * 3
    f[0] = a
    f[1] = b

    f[2] = xnor(a, b)
    if(n % 3 == 0):
        return f[2]
    else:
        return f[(n % 3) - 1]


def fib(a, b, n):
    f = [0] * 3
    f[0] = a
    f[1] = b
    f[2] = a ^ b
    if(n % 3 == 0):
        return f[2]
    else:
        return f[(n % 3) - 1]


def __starting_point():
    for _ in range(int(input())):
        a, b, n = list(map(int, input().split()))
        print(max(fib(a, b, n), xn(a, b, n)))


__starting_point()
