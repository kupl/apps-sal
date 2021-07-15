def row_weights(array):
    evens = []
    odd = []
    for i, el in enumerate(array):
        if i % 2 == 0:
            evens.append(el)
        else:
            odd.append(el)
    return sum(evens),sum(odd)
