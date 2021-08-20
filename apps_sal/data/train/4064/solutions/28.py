def count_by(x, n):
    multiples_of_x = []
    for number in range(1, n + 1):
        multiples_of_x.append(number * x)
    return multiples_of_x
    '\n    Return a sequence of numbers counting by `x` `n` times.\n    '
