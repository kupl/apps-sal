def row_weights(array):
    even = []
    odd = []
    for i,el in enumerate(array):
        if i % 2 == 0:
            even.append(el)
        else:
            odd.append(el)
    return sum(even), sum(odd)
