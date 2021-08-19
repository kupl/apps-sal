from itertools import chain
lines = '\n|  ###  |       |  ###  |  ###  |       |  ###  |  ###  |  ###  |  ###  |  ###  |       \n| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |       \n| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |       \n| #   # |     # |     # |     # | #   # | #     | #     |     # | #   # | #   # |       \n|       |       |  ###  |  ###  |  ###  |  ###  |  ###  |       |  ###  |  ###  |       \n| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |       \n| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |       \n| #   # |     # | #     |     # |     # |     # | #   # |     # | #   # |     # |       \n|  ###  |       |  ###  |  ###  |       |  ###  |  ###  |       |  ###  |  ###  |       \n'.lstrip().splitlines()


def digit_rotated(n):
    return [''.join((line[i] for line in lines)) for i in range(n * 8, (n + 1) * 8)]


def segment_display(n):
    digits = [int(c) for c in str(n)]
    if len(digits) < 6:
        digits = [-1] * (6 - len(digits)) + digits
    xs = (line for line in chain(*map(digit_rotated, digits), ['|||||||||']))
    return '\n'.join(map(''.join, zip(*xs)))
