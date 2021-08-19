def get_function(sequence):

    def res(x):
        return sequence[1] * x - sequence[0] * (x - 1)
    if any((res(x) - v for (x, v) in enumerate(sequence[2:], 2))):
        return 'Non-linear sequence'
    return res
