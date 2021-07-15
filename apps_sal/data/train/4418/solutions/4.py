def get_function(sequence):
    s0, s1 = sequence[:2]
    slope = s1 - s0
    if any(b - a != slope for a, b in zip(sequence[1:], sequence[2:])):
        return "Non-linear sequence"
    return lambda x: slope * x + s0
