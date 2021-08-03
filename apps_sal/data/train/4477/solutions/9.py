def reverse_number(n):

    result = 0
    is_neg = False

    if n < 0:
        n = -n
        is_neg = True

    while n != 0:
        result *= 10
        result += n % 10
        n = int(n / 10)

    if is_neg:
        return -result
    else:
        return result
