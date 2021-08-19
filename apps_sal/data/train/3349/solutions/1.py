def find_missing_number(sequence):
    try:
        numbers = sorted([int(x) for x in sequence.split()])
        for i in range(1, len(numbers) + 1):
            if i not in numbers:
                return i
    except ValueError:
        return 1
    return 0
