def multiple_of_index(xs):
    return [i for idx, i in enumerate(xs[1:]) if i % (idx + 1) == 0]
