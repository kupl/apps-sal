def is_very_even_number(n):
    return is_very_even_number(sum((int(i) for i in str(n)))) if n > 9 else not n % 2
