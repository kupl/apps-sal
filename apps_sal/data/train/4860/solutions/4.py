def amidakuji(arr):
    elements = list(range(len(arr[0]) + 1))
    for row in arr:
        for (i, col) in enumerate(row):
            if col == '1':
                (elements[i], elements[i + 1]) = (elements[i + 1], elements[i])
    return elements
