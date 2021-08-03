def find_missing_number(sequence):
    ns = sequence.split()
    numbers = {int(x) for x in ns if x.isdigit()}
    if len(numbers) != len(ns):
        return 1
    for i in range(1, max(numbers, default=0) + 1):
        if i not in numbers:
            return i
    return 0
