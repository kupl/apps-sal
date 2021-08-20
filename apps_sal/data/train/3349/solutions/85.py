def find_missing_number(sequence):
    if not sequence:
        return 0
    items = sequence.split(' ')
    numbers = []
    for item in items:
        try:
            numbers.append(int(item))
        except ValueError:
            return 1
    numbers.sort()
    if numbers[0] != 1:
        return 1
    for (i, x) in enumerate(numbers[:-1]):
        if numbers[i + 1] != x + 1:
            return x + 1
    return 0
