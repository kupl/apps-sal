def sum_of_minimums(numbers):
    n=0
    for lista in numbers:
        n+=min(lista)
    return n

