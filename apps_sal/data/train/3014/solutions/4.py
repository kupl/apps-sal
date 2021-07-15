def simple_transposition(text):
    row1 = []
    row2 = []
    count = 1
    for char in text:
        if count % 2 != 0:
            row1.append(char)
        else:
            row2.append(char)
        count += 1
    return ''.join(row1) + ''.join(row2)
