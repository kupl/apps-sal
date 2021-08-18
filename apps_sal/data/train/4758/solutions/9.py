def connect_four_place(columns):
    ls = [['-'] * 7, ['-'] * 7, ['-'] * 7, ['-'] * 7, ['-'] * 7, ['-'] * 7]
    for i, j in enumerate(columns):
        if i % 2 == 0:
            token = 'Y'
        else:
            token = 'R'
        z = 5
        while z >= 0:
            if ls[z][j] == '-':
                ls[z][j] = token
                break
            elif ls[z][j] != '-':
                z -= 1
    return ls
