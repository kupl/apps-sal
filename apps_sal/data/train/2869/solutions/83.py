def distinct(seq):
    numbers = []
    for elem in seq:
        if elem not in numbers:
            numbers.append(elem)
    return numbers
