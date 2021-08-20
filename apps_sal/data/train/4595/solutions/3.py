def on_left_diagonal(b1, b2):
    return b1[0] + b1[1] == b2[0] + b2[1]


def on_right_diagonal(b1, b2):
    return b1[0] - b2[0] == b1[1] - b2[1]


def bishop_diagonal(bishop1, bishop2):
    (b1, b2) = ((ord(bishop1[0]) - 96, int(bishop1[1])), (ord(bishop2[0]) - 96, int(bishop2[1])))
    if on_left_diagonal(b1, b2):
        key = b1[0] + b1[1]
        if key < 10:
            return ['a' + str(key - 1), chr(key + 95) + '1']
        else:
            return [chr(key + 88) + '8', 'h' + str(key - 8)]
    elif on_right_diagonal(b1, b2):
        if b1[0] >= b1[1]:
            return [chr(b1[0] - b1[1] + 97) + '1', 'h' + str(8 - b1[0] + b1[1])]
        else:
            return ['a' + str(b1[1] - b1[0] + 1), chr(b1[1] - b1[0] + 100) + '8']
    else:
        return sorted([bishop1, bishop2])
