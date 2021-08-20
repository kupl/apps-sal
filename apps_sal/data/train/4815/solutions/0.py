def is_very_even_number(n):
    while len(str(n)) > 1:
        n = sum((int(x) for x in str(n)))
    return True if n % 2 == 0 else False
