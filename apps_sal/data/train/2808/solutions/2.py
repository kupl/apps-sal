def polybius(text):
    square = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']
    ]

    encoded = ''
    for letter in text.replace('J', 'I'):
        if letter == ' ':
            encoded += ' '
        else:
            r = [i for i, row in enumerate(square) if letter in row][0]
            c = [row.index(letter) for row in square if letter in row][0]
            encoded += str(r + 1) + str(c + 1)
    encoded += ' '

    return encoded[:-1]
