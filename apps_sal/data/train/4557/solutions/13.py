def row_weights(array):
    group1 = []
    group2 = []
    for i in range(len(array)):
        if not i % 2:
            group1.append(array[i])
        else:
            group2.append(array[i])
    return (sum(group1), sum(group2))
