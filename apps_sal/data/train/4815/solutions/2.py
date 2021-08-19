def is_very_even_number(n):
    if n < 10:
        return n % 2 == 0
    return is_very_even_number(sum((int(d) for d in str(n))))
