def is_prime(num):
    square_num = int(num**0.5) + 1
    for divisor in range(2, square_num):
        if num % divisor == 0:
            return False
    return True


def gap(g, m, n):
    for num in range(m, n + 1):
        if (is_prime(num) and is_prime(num + g)
                and not any(is_prime(num1) for num1 in range(num + 1, num + g))):
            return [num, num + g]
            break
    return None
