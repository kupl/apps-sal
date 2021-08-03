mem = []


def sq_cub_rev_prime(n):
    x = mem[-1] + 1 if mem else 89
    while len(mem) < n:
        if is_prime(reverse(x**2)) and is_prime(reverse(x**3)):
            mem.append(x)
        x += 1
    return mem[n - 1]


def reverse(x):
    return int(str(x)[::-1])


def is_prime(x):
    return pow(2, x - 1, x) == 1
