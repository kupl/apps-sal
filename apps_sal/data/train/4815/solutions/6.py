def is_very_even_number(n):
    if len(str(n)) == 1:
        return n % 2 == 0
    return is_very_even_number(sum(map(int, list(str(n)))))
