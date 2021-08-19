def validate_sequence(a):
    return eval('=='.join([str(x) for x in [a[i] - a[i + 1] for i in range(len(a) - 1)]]))
