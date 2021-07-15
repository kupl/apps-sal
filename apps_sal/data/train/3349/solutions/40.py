def find_missing_number(sequence):
    if not sequence:
        return 0
    if not is_valid(sequence):
        return 1
    numbers = sorted([int(x) for x in sequence.split(' ')])
    n = 1
    for i in range(0, len(numbers)):
        if numbers[i] != n:
            return n
        n += 1
    return 0

def is_valid(sequence):
    numbers = sequence.split(' ')
    for a in numbers:
        if not a.isdigit():
            return False
    return True

