def two_highest(arg1):
    if arg1 == []:
        return []
    unique_integers = set(arg1)
    if len(unique_integers) == 1:
        return list(unique_integers)
    largest_integer = max(unique_integers)
    unique_integers.remove(largest_integer)

    second_largest_integer = max(unique_integers)

    return [largest_integer, second_largest_integer]
