def find_missing_number(sequence):
    if not sequence:
        return 0
    lst = sequence.split(" ")
    if not all([el.isdigit() for el in lst]):
        return 1
    lst = list([int(el) for el in lst])
    max_seq = max(lst)
    for el in range(1, max_seq + 1):
        if el not in lst:
            return el
    return 0
