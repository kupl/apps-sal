def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        numbers = sorted([int(x) for x in sequence.split()])
    except ValueError:
        return 1
    
    for i in range(1, len(numbers)+1):
        if i not in numbers:
            return i
    
    return 0

