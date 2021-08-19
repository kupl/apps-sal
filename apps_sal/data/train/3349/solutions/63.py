def find_missing_number(sequence):

    # проверка на не пустую строку
    if not sequence:
        return 0

    # проверка на int каждого элемента
    try:
        sequence = [int(elem) for elem in sequence.split()]
    except ValueError:
        return 1

    pattern = list(range(1, len(sequence) + 1))
    sequence.sort()

    for idx, elem in enumerate(sequence):
        if elem != pattern[idx]:
            return pattern[idx]

    return 0
