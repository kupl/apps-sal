cifer_sequence = [0, 1, 2, 0, 2, 3]


def cipher(phrase: str):
    crypt = ''
    for (i, simbol) in enumerate(phrase):
        if i < len(cifer_sequence):
            cifer_sequence.append(cifer_sequence[-3] + 1)
        if simbol == ' ':
            crypt += ' '
        else:
            crypt += chr((ord(simbol) - ord('a') + cifer_sequence[i]) % 26 + ord('a'))
    return crypt
