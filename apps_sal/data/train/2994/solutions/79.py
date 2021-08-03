def find_digit(num, nth):
    if nth < 1:
        return -1
    num = abs(num)
    d = nth - 1
    return (num // pow(10, d)) % 10
