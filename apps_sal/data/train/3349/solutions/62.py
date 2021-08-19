def find_missing_number(sequence):

    # проверка на не пустую строку
    if not sequence:
        return 0

    # проверка на int каждого элемента
    try:
        sequence = [int(elem) for elem in sequence.split()]
    except ValueError:
        return 1

    # проверка на совпадение
    for elem in range(1, len(sequence) + 1):
        if elem not in sequence:
            return elem

    return 0
