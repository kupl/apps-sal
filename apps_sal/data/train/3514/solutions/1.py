def validate_sequence(sequence):
    return sequence == list(range(sequence[0], sequence[-1] + 1, sequence[1] - sequence[0]))

