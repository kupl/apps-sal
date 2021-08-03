def cipher(str):
    key = [0, 1, 2, 0, 2, 3, 1, 3, 4, 2, 4, 5, 3, 5, 6, 4, 6, 7, 5, 7, 8, 6, 8, 9, 7, 9, 10, 8, 10, 11, 9, 11, 12, 10, 12, 13, 11, 13, 14, 12, 14, 15, 13, 15, 16, 14, 16, 17, 15, 17, 18, 16, 18, 19, 17, 19, 20, 18, 20, 21, 19, 21, 22, 20, 22, 23, 21, 23, 24, 22, 24, 25, 23, 25, 26]
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz' * 2

    for i in range(len(str)):
        if str[i] == ' ':
            result += ' '
            continue
        alpha_index = alphabet.find(str[i])
        result += alphabet[alpha_index + key[i]]
    return result
