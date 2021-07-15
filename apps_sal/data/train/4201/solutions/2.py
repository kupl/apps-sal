def find_missing(sequence):
    return (sequence[-1] + sequence[0]) * (len(sequence) + 1) / 2 - sum(sequence)

