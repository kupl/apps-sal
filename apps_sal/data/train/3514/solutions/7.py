def validate_sequence(sequence):
    increment = sequence[1] - sequence[0]
    return all((y - x == increment for (x, y) in zip(sequence, sequence[1:])))
