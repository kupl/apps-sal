def row_weights(array):
    odd = []
    even = []
    for i in range(len(array)):
        if i % 2 == 0:
            even.append(array[i])
            print(even)
        else:
            odd.append(array[i])
            print(odd)
    x = sum(odd)
    y = sum(even)
    return (y, x)
