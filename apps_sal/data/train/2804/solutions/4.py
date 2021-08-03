from itertools import cycle


def custom_christmas_tree(chars, height):
    ornament = cycle(chars)
    lines = []
    for n in range(1, height + 1):
        lines += [' ' * (height - n) + ' '.join(next(ornament) for _ in range(0, n))]
    for n in range(height // 3):
        lines += [' ' * (height - 1) + '|']
    return "\n".join(lines)
