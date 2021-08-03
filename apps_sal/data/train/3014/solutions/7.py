def simple_transposition(text):
    text = list(text)
    row1 = []
    row2 = []
    for x in range(len(text)):
        if x % 2 == 0:
            row1.append(text[x])
        else:
            row2.append(text[x])
    result = "".join(row1) + "".join(row2)
    return result
