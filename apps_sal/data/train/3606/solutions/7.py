def find_pattern(sequence):
    pattern = [a - b for (a, b) in zip(sequence[1:], sequence)]
    for size in range(1, len(pattern) + 1):
        if len(pattern) // size * pattern[:size] == pattern:
            return pattern[:size]
