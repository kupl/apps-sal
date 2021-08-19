def encode(message, key):
    alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    count = 0
    value = 0
    res = []
    n = len(message)
    key_index = list((i for i in str(key)))
    m_index = list((j for j in message))
    m = len(str(key)) - 1
    while count < n:
        res.append(alpha[m_index[count]] + int(key_index[value]))
        if value == m:
            value = 0
        else:
            value += 1
        count += 1
    print(res)
    return res
