def validate_sequence(sequence):
    step = sequence[1] - sequence[0]
    return all((b - a == step for (a, b) in zip(sequence, sequence[1:])))
