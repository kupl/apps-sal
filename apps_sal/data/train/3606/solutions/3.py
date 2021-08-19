def find_pattern(sequence):
    diff = [b - a for (a, b) in zip(sequence, sequence[1:])]
    return next((diff[:i] for i in range(1, len(diff) + 1) if diff[i:] + diff[:i] == diff))
