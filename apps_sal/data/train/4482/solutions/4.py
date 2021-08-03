from itertools import islice


def even_numbers_before_fixed(sequence, fixed_element):
    try:
        i = sequence.index(fixed_element)
    except ValueError:
        return -1
    return sum(x % 2 == 0 for x in islice(sequence, i))
