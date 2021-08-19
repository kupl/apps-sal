def max_tri_sum(numbers):
    no_duplicates = set(numbers)
    ordered = sorted(no_duplicates)
    return sum(ordered[-3:])
