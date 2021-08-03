def find_multiples(integer, limit):
    numbers = [i * integer for i in range(1, limit + 1) if (i * integer) <= limit]
    return numbers
