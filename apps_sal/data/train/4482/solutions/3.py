def even_numbers_before_fixed(sequence, fixed_element):
    if fixed_element in sequence:
        i = sequence.index(fixed_element)
        return sum((1 for n in sequence[:i] if n % 2 == 0))
    else:
        return -1
