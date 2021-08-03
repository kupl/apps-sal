def row_weights(array):
    a1, a2 = [], []
    row = [a1.append(array[i]) if i % 2 == 0 else a2.append(array[i]) for i in range(len(array))]
    return sum(a1), sum(a2)
