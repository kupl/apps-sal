def sum_even_numbers(seq):
    return sum((n for n in seq if not n % 2))
