from random import randint


def prime(n):
    if n < 4:
        return n == 2 or n == 3
    for i in range(5):
        a = randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def solve(n, k):
    if n < 2 * k:
        return (0)
    elif k == 1:
        if prime(n):
            return (1)
        else:
            return (0)
    elif k == 2:
        if n & 1:
            if prime(n - 2):
                return (1)
            else:
                return (0)
        else:
            return (1)
    else:
        return (1)


for t_itr in range(int(input())):
    n, k = list(map(int, input().split()))
    print(solve(n, k))
