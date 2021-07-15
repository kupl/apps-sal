def is_very_even_number(n):
    while n >= 10:
        n = sum(map(int, str(n)))
    return n % 2 == 0
