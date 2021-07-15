def even_numbers_before_fixed(sequence, fixed_element):
    try:
        return sum(elem % 2 == 0 for elem in sequence[:sequence.index(fixed_element)])
    except ValueError:
        return -1
