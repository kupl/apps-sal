def row_weights(array):
    even_index = []
    odd_index = []
    even_weight = 0
    odd_weight = 0
    for idx in range(len(array)):
        if idx % 2 != 0:
            odd_index.append(idx)
        else:
            even_index.append(idx)
    for i in even_index:
        even_weight += array[i]
    for i in odd_index:
        odd_weight += array[i]
    return (even_weight, odd_weight)
