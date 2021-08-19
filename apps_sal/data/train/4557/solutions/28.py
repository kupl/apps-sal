def row_weights(array):
    evens = []
    odds = []
    for (i, el) in enumerate(array):
        if i % 2 == 0:
            evens.append(el)
        else:
            odds.append(el)
    return (sum(evens), sum(odds))
