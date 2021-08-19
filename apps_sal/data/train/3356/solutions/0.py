def three_amigos(numbers):
    return min(([a, b, c] for (a, b, c) in zip(numbers, numbers[1:], numbers[2:]) if a & 1 == b & 1 == c & 1), key=lambda triple: max(triple) - min(triple), default=[])
