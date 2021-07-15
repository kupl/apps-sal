def even_numbers_before_fixed(sequence, fixed_element):
    return len(list(filter(lambda x: x % 2 == 0, sequence[:sequence.index(fixed_element)]))) if fixed_element in sequence else -1
