def pop_shift(input):
    input = list(input)
    x, y = list(), list()
    while len(input) > 1:
        x.append(input.pop())
        y.append(input.pop(0))
    return [''.join(x), ''.join(y), ''.join(input)]
