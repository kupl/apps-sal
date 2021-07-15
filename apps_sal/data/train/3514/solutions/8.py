def validate_sequence(sequence):
    i = sequence[1] - sequence[0]
    l = list(range(min(sequence),max(sequence)+1,i))
    return l == sequence
