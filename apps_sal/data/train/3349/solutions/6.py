def find_missing_number(sequence):
    try:
        numbers = sorted((int(word) for word in sequence.split(' ') if word))
    except ValueError:
        return 1
    return next((i + 1 for (i, n) in enumerate(numbers) if i + 1 != n), 0)
