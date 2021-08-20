def atomic_number(electrons):
    result = []
    i = 1
    while electrons > 0:
        result.append(min(2 * i ** 2, electrons))
        electrons -= result[-1]
        i += 1
    return result
