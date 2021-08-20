def amidakuji(ar):
    elements = list(range(len(ar[0]) + 1))
    for row in ar:
        for (i, col) in enumerate(row):
            if col == '1':
                (elements[i], elements[i + 1]) = (elements[i + 1], elements[i])
    return elements
