def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def max_even_digits_in_prime(n):
    return (len(str(n)) - 1) or 1


def count_of_even_digits(n):
    count = 0
    for i in str(n):
        count += (int(i) % 2 == 0)
    return count


def f(n):
    best_case = (0, 0)
    for x in range(n - 1, 1, -1):
        if is_prime(x):
            even_digits = count_of_even_digits(x)
            max_even_digits = max_even_digits_in_prime(x)
            if best_case[0] < even_digits:
                best_case = (even_digits, x)
            if max_even_digits == best_case[0]:
                print(best_case)
                return (best_case[1])
